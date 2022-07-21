
def main():
    extn = str(input("Input file name ").strip().lower())
    find(extn)


def find(extn):
    if "." in extn:
        ext = extn.split(".")
        x = int(len(ext)) - 1
        if ext[x] == ("jpg") or ext[x] == ("jpg"):
            print("image/jpeg")
        elif ext[x] == ("png"):
            print("image/png")
        elif ext[x] == "gif":
            print("image/gif")
        elif ext[x] == "pdf":
            print("application/pdf")
        elif ext[x] == "zip":
            print("application/zip")
        elif ext[x] == "txt":
            print("text/plain")
        else:
            print("application/octet-stream")
    else:
        print("application/octet-stream")

main()