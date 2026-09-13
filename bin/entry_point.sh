#!/bin/bash
set -euo pipefail

echo "Entry point script running"

CONFIG_FILE=_config.yml

# Function to manage Gemfile.lock
manage_gemfile_lock() {
    git config --global --add safe.directory '*'
    if [ -d .git ] && [ -f Gemfile.lock ]; then
        echo "Git checkout detected; keeping Gemfile.lock intact"
        git restore Gemfile.lock 2>/dev/null || true
    elif [ -f Gemfile.lock ]; then
        echo "No Git checkout detected; keeping Gemfile.lock for local preview"
    fi
}

start_jekyll() {
    manage_gemfile_lock
    bundle install --quiet
    bundle exec jekyll serve --watch --port=8080 --host=0.0.0.0 --livereload --verbose --trace --force_polling &
}

start_jekyll

while true; do
    inotifywait -q -e modify,move,create,delete $CONFIG_FILE
    if [ $? -eq 0 ]; then
        echo "Change detected to $CONFIG_FILE, restarting Jekyll"
        jekyll_pid=$(pgrep -f jekyll)
        kill -KILL $jekyll_pid
        start_jekyll
    fi
done
