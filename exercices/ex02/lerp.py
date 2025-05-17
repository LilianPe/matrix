from Vector import Vector
from Matrix import Matrix
from typing import List, TypeVar
from colorama import init, Fore

init(autoreset=True)
V = TypeVar('V')

def lerp(u: V, v: V, t: float) -> V :
	"""Make a linear interpolation from u to v at t"""
	if (t < 0 or t > 1) :
		print(Fore.RED + f"Error: t is invalid, must be beetwen 0 and 1, is {t}")
		return None
	if (type(u) != type(v)) :
		print(Fore.RED + f"Error: Incompatible types: u: {type(u)}, v: {type(v)}")
		return None
	if (type(u) == Matrix or type(u) == Vector) :
		if (u.getSize() != v.getSize()) :
			print(Fore.RED + f"Error: u and v have different sizes")
			return
		cpyu = u.copy()
		cpyu.scl(1 - t)
		cpyv = v.copy()
		cpyv.scl(t)
		cpyu.add(cpyv)
		return cpyu
	else :
		try :
			u *= (1 - t)
			v *= t
			return u + v
		except :
			print(Fore.RED + f"Error: Invalid types: {type(u)}")
			return None
