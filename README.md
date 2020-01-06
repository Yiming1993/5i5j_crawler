# 5i5j_crawler

## Introduction

A program crawling data from 5i5j.com. Data structure as:

{
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

Users can run xiangyu.py file and input a list of locations of Beijing to get house rental data. The data will be saved lcoally with MongoDB database.