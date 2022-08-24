'''
Question will be added in the later commit
'''

def getMaximumCouponValue(coupon, k):
	req_val = 0
	aplhabet_count = [0]*26
	val = 0
	for i in range(len(coupon) - (k-1)):
		for j in coupon[i: k+i]:
			aplhabet_count[ord(j) - 97] += 1
		for i in range(len(aplhabet_count)):
			if aplhabet_count[i] > 0:
				val += ((i+1) ** aplhabet_count[i]) % (10**9 + 7)
		if val > req_val:
			req_val = val
		val = 0
		aplhabet_count = [0]*26

	return req_val

def main():
	coupon_string, k_val = input().split()
	print(getMaximumCouponValue(coupon_string, int(k_val)))

if __name__ == '__main__':
	main()