#!/usr/bin/env bash

set -e -o pipefail

LAT=50.930581
LNG=5.780691

for tool in curl jq; do
    command -v "$tool" >/dev/null || { echo "ERROR: $tool missing"; exit 1; }
done

sun_data=$(curl -s "https://api.sunrise-sunset.org/json?lat=${LAT}&lng=${LNG}&formatted=0")
sunrise=$(date -d "$(jq -r '.results.sunrise' <<<"$sun_data")" +%s)
sunset=$(date -d "$(jq -r '.results.sunset' <<<"$sun_data")" +%s)
now=$(date +%s)

if (( now >= sunset || now <= sunrise )); then
    echo "ON"
else
    echo "OFF"
fi
