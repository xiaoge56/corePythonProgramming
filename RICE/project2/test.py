#coding:utf-8
import os
from lightning import Lightning
lgn = Lightning(host="http://rocky-river-8489.herokuapp.com/")
lgn.create_session('么么哒')

lgn.line([1,2,3,4,5,6,7,8,0,-2,2])
lgn.scatter([1,2,3],[2,9,4])
lgn.scatter([1,2,3],[2,9,4], label=[1,2,3], size=[5,10,20])
lgn.plot(data={"series": [1,2,3]}, type='line')
