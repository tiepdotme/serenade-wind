
# amp-jekyll and the challenges (errors) installing Nokogiri

Most useful resources:
 - [Nokogiri Install Tutorial](https://nokogiri.org/tutorials/installing_nokogiri.html#macos)
 - [StackExchange](https://apple.stackexchange.com/questions/254380/why-am-i-getting-an-invalid-active-developer-path-when-attempting-to-use-git-a)

## Nokogiri Install

|System|OS|Gem|Ruby|Bundler|Jekyll|
|------|--|---|----|-------|------|
|2011 MacBook Air|High Sierra, 10.13.6 (17G65)|v3.0.1|v2.6.0|v1.17.2|v3.8.5|

### Step 1 (the expected easy path)
After updating my Gemfile, I ran:
```bash
bundle install
```
The output (truncated for relevance):
```bash
Fetching nokogiri 1.10.9
Installing nokogiri 1.10.9 with native extensions
Gem::Ext::BuildError: ERROR: Failed to build gem native extension.
```
### Step2 (install direct via gem)
```bash
sudo gem install nokogiri -v '1.10.9'
```
Output:
```bash 
Building native extensions. This could take a while...
ERROR:  Error installing nokogiri:
    ERROR: Failed to build gem native extension.
```
### Step 3 (following stackoverflow instructions)
Source: [StackOverflow](https://stackoverflow.com/questions/46866828/ruby-nokogiri-gem-install-mac-osx-high-sierra), similar info found on [GitHub](https://github.com/sparklemotion/nokogiri/issues/1801)
```bash
gem install nokogiri -- --use-system-libraries=true --with-xml2-include="$(xcrun --show-sdk-path)"/usr/include/libxml2
```
Output:
```bash
xcrun: error: active developer path ("/Applications/Xcode.app/Contents/Developer") does not exist
Use `sudo xcode-select --switch path/to/Xcode.app` to specify the Xcode that you wish to use for command line developer tools, or use `xcode-select --install` to install the standalone command line developer tools.
See `man xcode-select` for more details.
Building native extensions with: '--use-system-libraries=true --with-xml2-include=/usr/include/libxml2'
This could take a while...
ERROR:  Error installing nokogiri:
    ERROR: Failed to build gem native extension.
```
### Step 4 (another  SO suggestion)
Apparently they found conflicts with *xz*
```bash
brew unlink xz
gem instal nokogiri
brew link xz
```
Output: 
```bash
Building native extensions. This could take a while...
ERROR:  Error installing nokogiri:
    ERROR: Failed to build gem native extension.
```
### Step 5
Looking at the xcode dependency to making this work.  This is mentioned in the [Nokogiri Install Tutorial](https://nokogiri.org/tutorials/installing_nokogiri.html#macos)
```bash
xcode-select --install
```
Output:
```bash
xcode-select: error: command line tools are already installed, use "Software Update" to install updates
```
Followed by:
```bash
sudo xcodebuild -license
```
Output:
```bash
xcrun: error: active developer path ("/Applications/Xcode.app/Contents/Developer") does not exist
Use `sudo xcode-select --switch path/to/Xcode.app` to specify the Xcode that you wish to use for command line developer tools, or use `xcode-select --install` to install the standalone command line developer tools.
See `man xcode-select` for more details.
```
### Step 6 (the one that works)
Having battled with the above, I searched to fix the *xcode* issue.  This [StackExchange](https://apple.stackexchange.com/questions/254380/why-am-i-getting-an-invalid-active-developer-path-when-attempting-to-use-git-a) answer yielded useful information/commands as follows:
```bash
sudo xcode-select --reset
sudo xcode-select --switch /Library/Developer/CommandLineTools
sudo gem install nokogiri
```
Output:
```bash
Building native extensions. This could take a while...
Successfully installed nokogiri-1.10.9
Parsing documentation for nokogiri-1.10.9
Installing ri documentation for nokogiri-1.10.9
Done installing documentation for nokogiri after 4 seconds
1 gem installed
```