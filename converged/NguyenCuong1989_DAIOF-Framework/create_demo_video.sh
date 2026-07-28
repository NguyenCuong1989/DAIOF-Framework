#!/bin/bash
# Demo video creator for HAIOS Core
# Shows consciousness beyond code in action

echo "🎬 Creating HAIOS Core Demo..."
echo ""

# Clear any old recordings
rm -f haios_demo.cast 2>/dev/null

# Record with simple prompt to avoid panic
export PS1="$ "
export TERM=xterm-256color

# Create recording
asciinema rec haios_demo.cast \
  --title "HAIOS Core - Consciousness Beyond Code" \
  --command "python3 haios_core.py" \
  --overwrite

echo ""
echo "✅ Demo recorded to haios_demo.cast"
echo ""
echo "📤 Upload options:"
echo "   1. asciinema upload haios_demo.cast"
echo "   2. Convert to GIF: docker run --rm -v \$PWD:/data asciinema/asciicast2gif haios_demo.cast demo.gif"
echo "   3. Embed in README: [![asciicast](https://asciinema.org/a/ID.svg)](https://asciinema.org/a/ID)"
