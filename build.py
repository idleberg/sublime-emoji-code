import os

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


    with open(outputFile, 'w') as file_:
        file_.write(output)


def plugin_loaded():
    from package_control import events

    # Get name of package
    me = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

    if events.install(me) or events.post_upgrade(me):

        print("Emoji Code: Building Snippets")

        outpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "snippets")

        if not os.path.exists(outpath):
            os.makedirs(outpath)

        # Let's go!
        write_completions("css", ".source.css, .source.sass", "content: '\\\\", "';")
        write_completions("html", ".text.html", "&#x", ";")
        write_completions("javascript", ".source.js", "\\\\u", "")
        write_completions("python", ".source.python", "u'\\\\U", "'")
        write_completions("ruby", ".source.ruby", "\\\\u{", "}")
