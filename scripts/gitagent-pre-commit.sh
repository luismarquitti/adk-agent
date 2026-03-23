#!/bin/bash
echo "Validating GitAgents..."
for dir in .agents/*; do
  if [ -d "$dir" ]; then
    echo "Validating $dir..."
    (cd "$dir" && npx @open-gitagent/gitagent validate) || exit 1
  fi
done
