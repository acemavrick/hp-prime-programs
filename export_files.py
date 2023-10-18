# program to process files stored in "python_programs" to "processed/"
# converts each file to a hp prime program (.hpprogram)

from os import scandir, remove


def write_python_wrapper(file):
    """Write a wrapper for the python program file."""
    print("Writing src file for " + file.name + "...", end="")
    name = file.name[:-3]

    output = f"""#PYTHON EXPORT {name}()\n\n"""
    with open(file, "r") as f:
        output += f.read()

    output += f"""\n#end"""

    with open(f"processed/{name}_src.hpprogram", "w") as f:
        f.write(output)
    print("done.")


def write_hpprogram(file):
    """Write a hp prime program file to run the python program file."""
    print("Writing command for " + file.name + "...", end="")
    name = file.name[:-3]
    output = f"""\
EXPORT {name}()
Begin
{name}()
End;"""
    with open(f"processed/{name}.hpprogram", "w") as f:
        f.write(output)
    print("done.")


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
                print("Processing " + file.name)
                write_python_wrapper(file)
                write_hpprogram(file)
                print("")
    print("Done processing files.")


if __name__ == "__main__": main()
