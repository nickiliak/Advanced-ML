#!/usr/bin/env bash
# Print per-week answered/total counts by inspecting Week*/answers/README.md.
# A question counts as "answered" when its block does NOT contain the
# placeholder "Add your answer here".

set -eu

repo_root="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$repo_root"

printf "%-7s %-9s %s\n" "Week" "Answered" "Topic"
printf "%-7s %-9s %s\n" "-----" "--------" "-----"

declare -A topics=(
  [1]="VAE / Deep Latent Variable Models"
  [2]="Normalizing Flows"
  [3]="Diffusion / DDPM"
  [5]="Manifold Learning & Latent Geometry"
  [6]="Metrics"
  [7]="Geometry"
  [9]="Graph Node Embeddings"
  [10]="GNNs — Graph Classification"
  [11]="Graph Convolutions"
)

for week in 1 2 3 5 6 7 9 10 11; do
  readme="Week${week}/answers/README.md"
  if [[ ! -f "$readme" ]]; then
    printf "%-7s %-9s %s\n" "Week${week}" "missing" "${topics[$week]}"
    continue
  fi
  total=$(grep -c "^## Question" "$readme" || true)
  empty=$(grep -c "Add your answer here" "$readme" || true)
  done_count=$((total - empty))
  printf "%-7s %-9s %s\n" "Week${week}" "${done_count}/${total}" "${topics[$week]}"
done
