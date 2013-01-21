
for f in AllFonts():
    hasEdits = False
    for name, members in f.groups.items():
        groupHasEdits = False
        new = []
        for m in members:
            if m[-1] == "'":
                groupHasEdits = True
                hasEdits = True
                new.append(m[:-1])
            else:
                new.append(m)
        f.groups[name]=new
        
    if hasEdits:
        print "edits made in ", f.info.fullName
        f.save()
    else:
        print "no edits made", f.info.fullName