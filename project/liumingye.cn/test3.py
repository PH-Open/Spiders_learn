# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/12 23:04
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import json

from selenium.webdriver.chrome.options import Options
import requests
from lxml import etree
from seleniumwire import webdriver
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
playlisturl = 'https://test.quanjian.com.cn/m/api/search/playlist'

browser = webdriver.Chrome(options=chrome_options)
# browser.get("https://tools.liumingye.cn/music/#/playlist/d7807039303?name=华语金曲千禧年前的旋律")
# sleep(10)
#
# def getmusiclist():
#     html = ''
#     for request in browser.requests:
#         if playlisturl in request.url:
#             playlist = request.response.body
#             html = html + playlist.decode('utf-8')
#             if playlist == None:
#                 continue
#             else:
#                 break
#     jsonlist = json.loads(html)
#     l = jsonlist['data']['list']
#     namelist = list(map(lambda x: x['name'], l))
#     return namelist
#
#
# namelist = getmusiclist()
# print(namelist)

namelist = ['若生命等候', '刀剑若梦', '连锁反应', '真的爱你', '浪子心声', '不装饰你的梦', '顺流逆流', '难得有情人', '堆积情感', '痴心换情深', '谁明浪子心', '上海滩',
            '等你等到我心痛', '千千阕歌', '最爱', '英雄泪', '我是一只小小鸟', '童年', '山丘', '飞鸟与鱼', '跟着感觉走', '爱，很简单', '有时候', '爱的呼唤', '铁血丹心',
            '想和你去吹吹风', '你快乐所以我快乐', 'Last Dance', '友情岁月', '浮躁', 'Lemon Tree', '掌心', '哭个痛快', '有心人', '如果云知道', '囚鸟',
            '没有人知的故事', '挪威的森林', '曲终人散', '夏夜晚风', '夜太黑', '忘记你我做不到', '为爱痴狂', '恋恋风尘', '红颜知己', '天下有情人', '当爱已成往事', '爱一回伤一回',
            '暧昧', '一千个伤心的理由', '十七岁的雨季', '为情所困', '恋曲2000', '爱江山更爱美人', '讲不出再见', '难得有情人(国)', '我不该看你的眼神', '问', '现在以后',
            '浪人情歌', '爱你十分泪七分', '太傻', '梦中人', '游戏人间', '味道', '矜持', '别怕我伤心', '偷心', '我期待', '刀剑如梦', '爱的故事(上)', '执迷不悔 (粤语版)',
            '用心良苦', '爱多一次痛多一次', '爱如潮水', '长路漫漫伴你闯', '谢谢你的爱', '明天我要嫁给你', '来生缘', '牵手', '老情歌', '如风往事', '夏日倾情', '飘雪', '旧朋友',
            '遥望', '容易受伤的女人', '孤单背影', '雨季不再来', '弯弯的月亮', '雨中的恋人们', '光辉岁月', '钟爱一生', '问情', '忘情森巴舞', '我悄悄蒙上你的眼睛', '满分情人',
            '一世情缘', '今夜你会不会来', '我用自己的方式爱你', '潇洒走一回', '漂洋过海来看你', '明天你是否依然爱我', '谁伴我闯荡', '一无所有', '男儿当自强 (国语)', '凡人歌',
            '一生心碎', '是不是每一个恋爱的人都像我', '让我欢喜让我忧', '如没有你', '一颗不变心', '为了爱 梦一生', '我是不是该安静的走开', '疯了', '每天爱你多一些', '人在黎明',
            '两个偶然', '别让明天的太阳离开我', '难舍难分', '他', '心的旅途', '似曾相识', '亲亲我的宝贝', '芳华绝代乱世佳人 (Lego Version)', '可否抱紧我', '给您留念',
            '谁明白爱', '其实我还是有些在乎', '共同渡过', '让爱自由', '夜未央', '醉人的一晚', '伤心的话留到明天再说', '雨夜倾情', '无名份的浪漫', '世外桃源', '伤尽我心的说话',
            '冬季来的女人', '卡拉永远OK', '可不可以', '季候风', '我和我追逐的梦', '爱恨缠绵', '光辉岁月', '敢爱敢做', '一生守候', '堆积情感', '滚滚红尘', '失恋阵线联盟',
            '最后的季节', '真的汉子', '珍重', '一千零一夜', '相逢在雨中', '李香兰', '如果你是我的传说', '风再起时(粤)', '月半小夜曲', '你怎么舍得我难过', '灰色轨迹', '哭砂',
            '情人的眼泪', '流浪的心', '我和春天有个约会', '相思无用', '心太软', '你的眼睛背叛你的心', '女人何苦为难女人', '傻瓜', '独角戏', '珍重', '情网', '痴心换情深',
            '当爱已成往事', '倩女幽魂', '玻璃之情', '一天到晚游泳的鱼', '你看你看月亮的脸', '约定', '女人花', '原来只要共你活一天', '短发', '回家', '只要为我爱一天',
            '多少柔情多少泪', '黄色月亮', '雪候鸟', '广岛之恋', '都是夜归人', '一生爱你千百回', '电台情歌', '那么爱你为什么', '白鸽', 'DEAR JOHN', '三万英尺', '中意他',
            '百年孤寂', '爱江山更爱美人', '春夏秋冬', '李香兰', '半点心', '我', '渡口', '大海', '红豆', '吻别', '水手', '朋友', '太傻', '伤痕', '领悟', '值得',
            '友情岁月', '爱与哀愁', '对你爱不完', '宝贝对不起', '谁的眼泪在飞', '我的未来不是梦', '风中有朵雨做的云', '最爱', '忘记他', '护花使者', '朋友别哭', '新不了情',
            '海阔天空', '一言难尽', '别问我是谁', '你把我灌醉', '再回到从前', '大约在冬季', '我想有个家', '新鸳鸯蝴蝶梦', '每天爱你多一些', '人生何处不相逢', '冬季到台北来看雨',
            '只要你过得比我好', '爱我的人和我爱的人', '大地', '情人', '情书', '慢慢', '祈祷', '胆小鬼', '铿锵玫瑰', '不再犹豫', '沉默是金', '他不爱我', '男人的好',
            '爱的代价', '孤枕难眠 (Live)', '愚人码头', '阳光总在风雨后', '恋曲1990', '怪你过份美丽', '新不了情', '为你我受冷风吹', '爱上一个不回家的人', '独家记忆',
            '你最珍贵', '囚鸟(国)', '一生所爱', '你是我胸口永远的痛', '我有我天地', '天才白痴梦', '来生缘', '星星点灯', '单身情歌', '友谊之光', '爱如潮水',
            "春夏秋冬 A Balloon's Journey", '天下有情人', '当我眼前只有你', '人生如此', '滚滚红尘', '初恋情人', '梦醒时分', '归来吧', '亲密爱人(Live)',
            '容易受伤的女人', '天若有情', '为你我受冷风吹', '再见亦是泪', '灰色轨迹', '忘情冷雨夜', '堆积情感', '恋曲1980', '情深海更深', '爱就一个字', '冬天里的一把火',
            '故乡的云', '爱我别走', '胆小鬼', '雨一直下', '秋去秋来', '祝你一路顺风', '滚滚红尘', '你怎么舍得我难过', '最浪漫的事', '神话·情话', '让我欢喜让我忧', '伤心太平洋',
            '追梦人', '漫步人生路', '人生何处不相逢', '失恋', '爱的传说']

# browser.quit()

# sleep(2)
cnt = 0
musiclist = []
for name in namelist:
    # name = namelist[3]
    url_1 = 'https://music.163.com/#/search/m/?s=' + name + '&type=1'
    # 初始化browser对象
    # 访问该url
    browser.get(url=url_1)
    # 由于网页中有iframe框架，进行切换
    browser.switch_to.frame('g_iframe')
    # 等待0.5秒
    sleep(0.5)
    # 抓取到页面信息
    page_text = browser.execute_script("return document.documentElement.outerHTML")
    # print(page_text)
    # 退出浏览器
    tree = etree.HTML(page_text)
    try:
        id = tree.xpath("/html/body/div[3]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/a/@data-res-id")[0]
        cnt += 1
        url = f'http://music.163.com/song/media/outer/url?id={id}'
        musiclist.append((name, url))
    except:
        pass
    sleep(1)
browser.quit()
print(musiclist)
print(cnt)
