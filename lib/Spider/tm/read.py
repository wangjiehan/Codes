import json
import os
import numpy as np

print("Running from", os.path.dirname(os.path.realpath(__file__)))

class GetCommentsFromJson():
    def __init__(self, first_dir, second_dir):
        self.first_dir = first_dir
        self.second_dir = second_dir
        file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "jsonfile/%s/%s/" % (self.first_dir, self.second_dir))
        a = self.file_path(file_dir)
        self.file_list = a[1]

    def file_path(self, file_dir):
        for root, dirs, files in os.walk(file_dir):
            return root, files

    def get_comments(self):
        comments = []
        ids = []
        for filename in self.file_list:
            id_ = filename.split(".")[0]
            ids.append(id_)
            files = os.path.join(os.path.dirname(os.path.realpath(__file__)), "jsonfile/%s/%s/" % (self.first_dir, self.second_dir) + filename)
            with open(files, "r") as f:
                txt = json.load(f)
                # print(files)
                # time.sleep(2)
                single_product_comments = []
                for i in range(len(txt)):
                    single_product_comments.append(txt[i]["rateContent"])
                comments.append(single_product_comments)
        return comments, ids

    def to_npy(self, comments):
        np.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/comments.npy"), comments)

    def to_txt(self, comments):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/comments.txt"), "w", encoding='utf-8') as f:
            for comments_ in comments:
                # print(comments_)
                for comment in comments_:
                    print(comment)
                    f.write(comment)
                    f.write("\n")

    def main(self):
        comments = self.get_comments()
        # to_npy(comments)
        # to_txt(comments)
        # 二维数组，60件商品，每件商品多条评论
        return comments

if __name__ == "__main__":
    a = GetCommentsFromJson("beauty", "欧莱雅")
    a.main()
