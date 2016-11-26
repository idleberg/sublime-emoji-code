import os, sublime, sublime_plugin

def plugin_loaded():
    from package_control import events

    me = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

    if events.install(me) or events.post_upgrade(me):
        build()

class BuildSnippetsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        build()

# Helper Functions

def write_completions(type, scope, prefix, suffix):
    import json
    from emojitations import emoji

    completions = []

    for attr, value in emoji.__dict__.items():
        try:
            slug    = emoji.en[attr].slug.replace("_", "-")
            literal = emoji.en[attr].emoji

            codepoint = hex(emoji.en[attr].codepoints[0]).split('x')[1]

            body = prefix + codepoint + suffix
            trigger  = "ji:" + slug + "\t" + literal

            completions.append({"contents": body, "trigger": trigger})
        except:
            pass

    snippets = {
        "scope": scope,
        "completions": completions
    }

    output = json.dumps(snippets, sort_keys=True, indent=True, separators=(',', ': '), ensure_ascii=False)
    outputFile = os.path.join(os.path.dirname(os.path.realpath(__file__)), "snippets", 'emoji-'+type+'.sublime-completions')

    with open(outputFile, 'w') as file:
        print("Emoji Code: Creating \"%s\"" % outputFile)
        file.write(output)

def build():
    print("Emoji Code: Building Snippets")

    make_directory()
    make_completions()

def make_directory():
    outpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "snippets")

    if not os.path.exists(outpath):
        os.makedirs(outpath)

def make_completions():
    write_completions("css", ".source.css, .source.sass", "content: '\\\\", "';")
    write_completions("html", ".text.html", "&#x", ";")
    write_completions("javascript", ".source.js", "\\\\u", "")
    write_completions("python", ".source.python", "u'\\\\U", "'")
    write_completions("ruby", ".source.ruby", "\\\\u{", "}")
