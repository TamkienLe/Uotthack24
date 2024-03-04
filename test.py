import algo 

footprint = algo.material_footprint(algo.makeup) + algo.shipping_footprint(algo.coa)
water = algo.water_usage(algo.makeup)

print(f"Your brand's ethical manufacturing practice is rated {algo.brand_score}/100")