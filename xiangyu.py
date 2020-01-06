import crawler_crawl_ip
import crawler_make_header
import crawler_connect_web
import crawler_info_extract
import config
import time_service
import mongoDB_services
from urllib.parse import quote
import math


class Xiangyu(object):
    def __init__(self):
        self.db = config.db_me('NEWS')
        self.header = {"User-Agent":crawler_make_header.make_agent(),
                       "Referer":"http://www.1zu.com/house/bj/houseList.htm?searchName={}&isAms={}&rentType={}",
                       "Origin": "http://www.1zu.com",
                       "Host":"www.1zu.com",
                       "Cookie":"",
                       "Accept":"*/*",
                       "X-Requested-With": "XMLHttpRequest"}
        self.origin_path = config.origin_path()
        self.proxy_path = self.origin_path + '/References/proxy.txt'

    def make_data(self, search_name, page_num):
        data = {
            "MIME类型": "application/x-www-form-urlencoded;charset=UTF-8",
            "pageNum": page_num,
            "searchStr": search_name,
            "rentType": 1,
            "inDistrict":"",
            "businessCircleCd":"",
            "minPrice":"",
            "maxPrice":"",
            "houseType":"",
            "orderByType":"",
            "subwayStations":"",
            "subwayLines":"",
            "flag": 0,
            "commissionDiscountFlag":"",
            "shortRental":"",
            "vacantStartDate":"",
            "rientation":"",
            "areaMin":"",
            "areaMax":"",
            "isToilet":"",
            "isBalcony":"",
            "isYerornoSubway":"",
            "isRate":""
        }
        return data

    def ratio_score(self, distance, size, price, direction, room_num, price_threhold=5000):
        if distance != None:
            distance = int(distance)
        size = int(size)
        price = int(price)
        room_num = int(room_num)

        if distance == None:
            distance = 0

        score = int(20000-price) + size * 10 + distance * 0.5

        if direction != None:
            if '南' in direction:
                score = score * 1.5
            if '东' in direction:
                score = score * 1.2

        if price < price_threhold and room_num == 1:
            score = score * 2

        if price - price_threhold > 1500 and room_num == 1:
            score = score * 0.5

        return score

    def work_flow(self, search_names):
        house_list = []
        for search_name in search_names:
            link_request = "http://www.1zu.com/house/bj/houseList.htm?searchName={}&isAms=1&rentType=1".format(quote(search_name))
            link = "http://www.1zu.com/house/bj/houseListAjax.htm"
            for i in range(10):
                self.header["Referer"] = link_request
                proxy = crawler_crawl_ip.get_random_ip(self.proxy_path)
                data = self.make_data(search_name,i)

                data_dict = crawler_connect_web.get_post(link, data, self.header, proxy)
                for data in self.decode_data(data_dict):
                    score = self.ratio_score(data["distance"], data["size"], data["price"], data["direction"], data["room_num"])
                    house_list.append((data["link"], score))
        sorted_list = sorted(set(house_list), key=lambda x:x[1], reverse = True)
        sorted_list = [i[0] for i in sorted_list]
        for i in sorted_list:
            print(i)

    def decode_data(self, data_dict):
        data_dict = crawler_info_extract.json_extract(data_dict)
        data_list = data_dict["data"]["results"]

        for data_dict in data_list:
            data_out = {
                "house_name":data_dict["projectName"],
                "direction":data_dict["dictName"],
                "circle":data_dict["circle"],
                "floor":data_dict["floor"],
                "kitchen":data_dict["fewKitchen"],
                "toilet":data_dict["fewToilet"],
                "station":data_dict["station"],
                "price":data_dict["rentPrice"],
                "distance":data_dict["distance"],
                "start_vacant":time_service.timestamp2time(str(data_dict["vacantStartDate"])[:10]),
                "room_num":data_dict["fewRoom"],
                "size":data_dict["area"],
                "pic":data_dict["fmpic"],
                "link":"http://www.1zu.com/house/bj/houseDetail.htm?houseId={}&roomId=0&rentType=1".format(data_dict["houseId"])
            }
            yield data_out


if __name__ == '__main__':
    X = Xiangyu()
    search_list = []
    X.work_flow(search_list)
