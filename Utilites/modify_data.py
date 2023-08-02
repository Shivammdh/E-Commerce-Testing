class ModifyData:

    def modify_price_data(self,flipkart_price,amazon_price,corma_price):
        p1, p2, p3 = flipkart_price[1:], amazon_price, corma_price[1:]
        ip1, ip2, ip3 = [v1 for v1 in p1 if v1 != ','], [v2 for v2 in p2 if v2 != ','], [v3 for v3 in p3 if v3 != ',']
        f_p, a_p, c_p = int(''.join(ip1)), int(''.join(ip2)), int(float(''.join(ip3)))
        prices = [f_p, a_p, c_p]
        return prices

    def modify_people_rate_data(self,flipkart_people_rate,amazon_pepol_rate,corma_pepole_rating):
        f_rate, a_rate, c_rate = int(flipkart_people_rate.split()[0]), int(amazon_pepol_rate.split()[0]), int(
            corma_pepole_rating.split()[0])
        total_peoples_rating = [f_rate, a_rate, c_rate]
        return total_peoples_rating

    def modify_reviews(self,flipkart_review,amazon_review,corma_pepole_review):
        f_reviw, a_review, c_review = int(flipkart_review.split()[0]), int(amazon_review.split()[0]), int(
            corma_pepole_review.split()[0])
        reviews=[f_reviw, a_review, c_review]
        return reviews

    def modify_rating_in_stars(self, flipkart_rating, amazon_rating, corma_rating):
        flipkart_stars, amazon_stars, corma_stars = float(flipkart_rating), float(amazon_rating), float(corma_rating)
        ratings = [flipkart_stars, amazon_stars, corma_stars]
        return ratings