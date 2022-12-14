from prop_session import *

ex69ref = \
  [(Text('Example 6.9  a & b |- ~(~a v ~b)'), comment),
    (And(a,b), given),
    (a, aer, 1),
    (b, ael, 1),
    (Or(Not(a),Not(b)), assume),
    (Not(a), assume),
    (F, contra, 2,5),
    (Not(Not(a)), raa, 5,6),
    (Not(b), oel, 4,7),
    (F, contra, 3,8),
    (Not(Or(Not(a),Not(b))), raa, 4,9)]

print(check_proof(ex69ref))
