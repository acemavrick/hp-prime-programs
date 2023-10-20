# program to process files stored in "python_programs" to "processed/"
# converts each file to a hp prime program (.hpprogram)

from os import scandir, remove


def main():
    """Main processing program."""
    clearProccessed = True

    processed_dirname = "processed"
    srcPrograms_dirname = "python_programs"

    if clearProccessed:
        print("Clearing processed directory...", end="")
        for file in scandir(processed_dirname):
            remove(file.path)
        print("done.")

    print("\nProcessing files from\"", srcPrograms_dirname, "\"to\"", processed_dirname, "\"\n")

    src_scanner = scandir(srcPrograms_dirname)

    # go through each file in the source directory
    while (True):
        try:
            file = next(src_scanner)
        except StopIteration:
            # done
            break
        else:
            # process the file

            # check if the file is a python program
            if file.name.endswith(".py"):
                print("Processing " + file.name + "...", end="")

                name = file.name[:-3]
                output = """#PYTHON wrapper\n"""
                output += f"""print("\\n" + "="*5 + {file.name} + "="*5+"\n")\n"""
                with open(file, "r") as f:
                    output += f.read()

                output += f"""\n#END"""
                output += f"""\nEXPORT {name}()"""
                output += """\n    PYTHON(wrapper)"""
                output += """\nEND;"""

                with open(f"processed/{name}.txt", "w") as f:
                    f.write(output)
                print("done.")
                print("")
    print("Done processing files.")


if __name__ == "__main__": main()
