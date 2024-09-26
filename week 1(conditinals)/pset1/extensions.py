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