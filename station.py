"""
import requests
import re
import pprint
#生成字典 运行一次后抛弃之~~~
def new_dictionary():
    url="https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9069"
    station_namesweb=requests.get(url)
    stationdic = re.findall(r'([\u4e00-\u9fa5]+)\|([a-zA-Z]+)', station_namesweb.text)
    stationdic=dict(stationdic)
    pprint.pprint(stationdic)
new_dictionary()
"""
stations={
    '北京':'BJS',
    '上海':'SHA',
    '广州':'CAN',
    '深圳':'SZX',
    '成都':'CTU',
    '杭州':'HGH',
    '武汉':'WUH',
    '西安':'SIA',
    '重庆':'CKG',
    '青岛':'TAO',
    '长沙':'CSX',
    '南京':'NKG',
    '厦门':'XMN',
    '昆明':'KMG',
    '大连':'DLC',
    '天津':'TSN',
    '郑州':'CGO',
    '三亚':'SYX',
    '济南':'TNA',
    '福州':'FOC',
    '阿勒泰':'AAT',
    '阿克苏':'AKU',
    '鞍山':'AOG',
    '安庆':'AQG',
    '安顺':'AVA',
    '阿拉善左旗':'AXF',
    '中国澳门':'MFM',
    '阿里':'NGQ',
    '阿拉善右旗':'RHT',
    '阿尔山':'YIE',
    '巴中':'BZX',
    '百色':'AEB',
    '包头':'BAV',
    '毕节':'BFJ',
    '北海':'BHY',
    '北京(大兴国际机场)':'BJS,PKX',
    '北京(首都国际机场)':'BJS,PEK',
    '博乐':'BPL',
    '保山':'BSD',
    '白城':'DBC',
    '布尔津':'KJI',
    '白山':'NBS',
    '巴彦淖尔':'RLK',
    '昌都':'BPX',
    '承德':'CDE',
    '常德':'CGD',
    '长春':'CGQ',
    '朝阳':'CHG',
    '赤峰':'CIF',
    '长治':'CIH',
    '沧源':'CWJ',
    '常州':'CZX',
    '池州':'JUH',
    '大同':'DAT',
    '达州':'DAX',
    '稻城':'DCY',
    '丹东':'DDG',
    '迪庆':'DIG',
    '大理':'DLU',
    '敦煌':'DNH',
    '东营':'DOY',
    '大庆':'DQA',
    '德令哈':'HXD',
    '鄂尔多斯':'DSN',
    '额济纳旗':'EJN',
    '恩施':'ENH',
    '二连浩特':'ERL',
    '阜阳':'FUG',
    '抚远':'FYJ',
    '富蕴':'FYN',
    '果洛':'GMQ',
    '格尔木':'GOQ',
    '广元':'GYS',
    '固原':'GYU',
    '中国高雄':'KHH',
    '赣州':'KOW',
    '贵阳':'KWE',
    '桂林':'KWL', '红原':'AHJ', '海口':'HAK', '河池':'HCJ', '邯郸':'HDG', '黑河':'HEK', '呼和浩特':'HET', '合肥':'HFE', '淮安':'HIA', '怀化':'HJJ', '海拉尔':'HLD', '哈密':'HMI', '衡阳':'HNY', '哈尔滨':'HRB', '和田':'HTN', '花土沟':'HTT', '中国花莲':'HUN', '霍林郭勒':'HUO', '惠州':'HUZ', '汉中':'HZG', '黄山':'TXN', '呼伦贝尔':'XRQ', '中国嘉义':'CYI', '景德镇':'JDZ', '加格达奇':'JGD', '嘉峪关':'JGN', '井冈山':'JGS', '金昌':'JIC', '九江':'JIU', '荆门':'JM1', '佳木斯':'JMU', '济宁':'JNG', '锦州':'JNZ', '建三江':'JSJ', '鸡西':'JXA', '九寨沟':'JZH', '中国金门':'KNH', '揭阳':'SWA', '库车':'KCA', '康定':'KGT', '喀什':'KHG', '凯里':'KJH', '库尔勒':'KRL', '克拉玛依':'KRY', '黎平':'HZH', '澜沧':'JMJ', '龙岩':'LCX', '临汾':'LFQ', '兰州':'LHW', '丽江':'LJG', '荔波':'LLB', '吕梁':'LLV', '临沧':'LNJ', '陇南':'LNL', '六盘水':'LPF', '拉萨':'LXA', '洛阳':'LYA', '连云港':'LYG', '临沂':'LYI', '柳州':'LZH', '泸州':'LZO', '林芝':'LZY', '芒市':'LUM', '牡丹江':'MDG', '中国马祖':'MFK', '绵阳':'MIG', '梅州':'MXZ', '中国马公':'MZG', '满洲里':'NZH', '漠河':'OHE', '南昌':'KHN', '中国南竿':'LZN', '南充':'NAO', '宁波':'NGB', '宁蒗':'NLH', '南宁':'NNG', '南阳':'NNY', '南通':'NTG', '攀枝花':'PZI', '普洱':'SYM', '琼海':'BAR', '秦皇岛':'BPE', '祁连':'HBQ', '且末':'IQM', '庆阳':'IQN', '黔江':'JIQ', '泉州':'JJN', '衢州':'JUZ', '齐齐哈尔':'NDG', '日照':'RIZ', '日喀则':'RKZ', '若羌':'RQA', '神农架':'HPG', '莎车':'QSZ', '沈阳':'SHE', '石河子':'SHF', '石家庄':'SJW', '上饶':'SQD', '三明':'SQJ', '十堰':'WDS', '邵阳':'WGN', '松原':'YSQ', '台州':'HYN', '中国台中':'RMQ', '塔城':'TCG', '腾冲':'TCZ', '铜仁':'TEN', '通辽':'TGO', '天水':'THQ', '吐鲁番':'TLQ', '通化':'TNH', '中国台南':'TNN', '中国台北':'TPE', '中国台东':'TTT', '唐山':'TVS', '太原':'TYN', '五大连池':'DTU', '乌兰浩特':'HLH', '乌兰察布':'UCB', '乌鲁木齐':'URC', '潍坊':'WEF', '威海':'WEH', '文山':'WNH', '温州':'WNZ', '乌海':'WUA', '武夷山':'WUS', '无锡':'WUX', '梧州':'WUZ', '万州':'WXN', '乌拉特中旗':'WZQ', '巫山':'WSK', '兴义':'ACX', '夏河':'GXH', '中国香港':'HKG', '西双版纳':'JHG', '新源':'NLT', '忻州':'WUT', '信阳':'XAI', '襄阳':'XFN', '西昌':'XIC', '锡林浩特':'XIL', '西宁':'XNN', '徐州':'XUZ', '延安':'ENY', '银川':'INC', '伊春':'LDS', '永州':'LLF', '榆林':'UYN', '宜宾':'YBP', '运城':'YCU', '宜春':'YIC', '宜昌':'YIH', '伊宁':'YIN', '义乌':'YIW', '营口':'YKH', '延吉':'YNJ', '烟台':'YNT', '盐城':'YNZ', '扬州':'YTY', '玉树':'YUS', '岳阳':'YYA', '张家界':'DYG', '舟山':'HSN', '扎兰屯':'NZL', '张掖':'YZY', '昭通':'ZAT', '湛江':'ZHA', '中卫':'ZHY', '张家口':'ZQZ', '珠海':'ZUH', '遵义':'ZYI'
}