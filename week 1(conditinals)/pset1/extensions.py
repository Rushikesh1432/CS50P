#In a file called extensions.py, implement a program that prompts the user for the name 
# of a file and then outputs that file’s media type if the file’s name ends,
# case-insensitively, in any of these suffixes:
#refer this link "developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types"

s=str(input("Enter file Name:")).lower().strip()


if s.endswith("gif"):
    print("Image/gif")

elif s.endswith("jpg") or s.endswith("jpeg"):
    print("image/jpeg")

elif s.endswith("png"):
    print("image/png")

elif s.endswith("pdf"):
    print("application/pdf")

elif s.endswith("txt"):
    print("text/plain")

elif s.endswith("zip"):
    print("application/zip")

elif s.endswith("aac"):
    print("Audio/acc")

elif s.endswith("mp4"):
    print("video/mp4")

else:
    print("application/octet-stream")