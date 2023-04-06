def solution(chicken):
    service = 0
    coupon = chicken
    
    while coupon >= 10:
        ate = coupon // 10
        service += ate
        coupon = coupon % 10 + ate
    return service