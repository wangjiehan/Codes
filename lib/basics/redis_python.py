import redis
import json
import datetime

extime = datetime.datetime(2019, 9, 30, 00, 00, 00)


class RedisPython():
    def __init__(self, redis_config):
        self.config = redis_config
        self.r = redis.StrictRedis(**self.config)

    # pipeline 的方式写入 list 的 value
    def _insert_list_pipeline(self, key, rec_list):
        pipe = self.r.pipeline()
        pipe.delete(key)
        pipe.rpush(key, *rec_list)

        # pipe.expire(key, 86400)       # 设置过期时间为 86400 秒
        # pipe.expireat(key, extime)    # 具体到哪一时刻过期

        pipe.execute()

    # 单条写入 list 的 value
    def _insert_list(self, key, rec_list):
        self.r.delete(key)
        self.r.rpush(key, *rec_list)

        # self.r.expire(key, 86400)
        # self.r.expireat(key, extime)

    def _insert_dict_str(self, key, _dict):
        # json.dump(dict) 可以把字典 dict 序列化成一个json格式的字符串，写入 redis
        def dic2json_str(dictionary):
            return json.dumps(dictionary)

        json_str = dic2json_str(_dict)
        self.r.delete(key)
        self.r.set(key, json_str)

        # self.r.expire(key, 86400)
        # self.r.expireat(key, extime)

    # 查询共有多少条该 prefix 的 key 的数据
    def _count(self, prefix):
        return len(self.r.keys(str(prefix) + "*"))

    def _read_data(self, key_list):
        log = ""
        for key in key_list:
            log += str(key) + ": " + self.r.lrange(key, 0, -1) + "\n"
        return log.strip()


if __name__ == "__main__":
    REC_REDIS_CONFIG = {
        'host': 'r-2zeb79a5e8639d14.redis.rds.aliyuncs.com',
        'port': 6379,
        'password': 'KCTsB%5KXcQY',
        'decode_responses': True
    }

    r = RedisPython(REC_REDIS_CONFIG)

    print(r._count("mt_channel_"))
