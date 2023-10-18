pydoc-markdown

# Check for OS
if [[ "$OSTYPE" == "darwin"* ]]; then
  # Mac OS uses gsed
  command -v gsed >/dev/null 2>&1 || { echo >&2 "Requires gsed but it's not installed. Try installing it using 'brew install gnu-sed'."; exit 1; }
  # Update Table Of Content: remove "ask_dubo"
  gsed -zi 's/\* \[ask\\_dubo\](#ask\_dubo)\n//g' DOC.md
  gsed -i 's/  \* /\* /g' DOC.md
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  # Linux uses sed
  sed -zi 's/\* \[ask\\_dubo\](#ask\_dubo)\n//g' DOC.md
  sed -i 's/  \* /\* /g' DOC.md
else
  # Unknown OS
  echo "Your OS is not supported."
  exit 1
fi
