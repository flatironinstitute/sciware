# MATLAB real-world optics example

This is actually a rather typical research code exchange situation.

Discuss the utility of the following function, that Alex needed to compare
against in optics:

[bdfw.m.orig](https://github.com/ahbarnett/fresnaq/blob/master/bdrymeths/bdwf.m.orig)

What would be needed to make it usable? (don't go into the weeds here, just
big picture...)

Here is a more usable version:

[bdwf.m](https://github.com/ahbarnett/fresnaq/blob/master/bdrymeths/bdwf.m)

plus

[test_bdwf.m](https://github.com/ahbarnett/fresnaq/blob/master/bdrymeths/test_bdwf.m)

Did that match your usibility criteria?

Finally, what changes from that interface were done here: ?

[bdfw_pts.m](https://github.com/ahbarnett/fresnaq/blob/master/bdrymeths/bdwf_pts.m)

Discuss advantage/disadvantage of this new interface, from the user side.
*Hints: focus on (xi,eta) in the docs. A basic discussion needs docs only; a full discussion requires some parsing of the code... have fun.*
