def greeting(name,lang):
    languages = {
        "en": "hello",
        "es": "hola",
        "fr": "bonjour"
    }
    msg = f"{languages[lang.lower()]} {name}"
    print(msg)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="A simple greeting")
    parser.add_argument(
        "-n", "--name", metavar="name", dest="greet", help="name of the person to greet", required=True
        )
    
    parser.add_argument(
        "-l","--lang", metavar="lang", dest="lang", help="langauge of the greeting", choices = ["en","es","fr"],required=True
    )

    args = parser.parse_args()

    greeting(args.greet,args.lang)