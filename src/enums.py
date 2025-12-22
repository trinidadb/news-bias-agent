from enum import Enum


class NewsCategory(str, Enum):
    BUSINESS = 'business'
    ENTERTAINMENT = 'entertainment'
    GENERAL = 'general'
    HEALTH = 'health'
    SCIENCE = 'science'
    SPORTS = 'sports'
    TECHNOLOGY = 'technology'


class SortBy(str, Enum):
    RELEVANCY = "relevancy"
    POPULARITY = "popularity"
    PUBLISHED_AT = "publishedAt"


class SearchIn(str, Enum):
    TITLE = "title"
    DESCRIPTION = "description"
    CONTENT = "content"


class Language(str, Enum):
    ARABIC = 'ar'
    GERMAN = 'de'
    ENGLISH = 'en'
    SPANISH = 'es'
    FRENCH = 'fr'
    HEBREW = 'he'
    ITALIAN = 'it'
    DUTCH = 'nl'
    NORWEGIAN = 'no'
    PORTUGUESE = 'pt'
    RUSSIAN = 'ru'
    SWEDISH = 'sv'
    UD = 'ud'  # 'ud' is non-standard, likely Undefined in this API
    CHINESE = 'zh'


class Country(str, Enum):
    UNITED_ARAB_EMIRATES = 'ae'
    ARGENTINA = 'ar'
    AUSTRIA = 'at'
    AUSTRALIA = 'au'
    BELGIUM = 'be'
    BULGARIA = 'bg'
    BRAZIL = 'br'
    CANADA = 'ca'
    SWITZERLAND = 'ch'
    CHINA = 'cn'
    COLOMBIA = 'co'
    CUBA = 'cu'
    CZECH_REPUBLIC = 'cz'
    GERMANY = 'de'
    EGYPT = 'eg'
    FRANCE = 'fr'
    UNITED_KINGDOM = 'gb'
    GREECE = 'gr'
    HONG_KONG = 'hk'
    HUNGARY = 'hu'
    INDONESIA = 'id'
    IRELAND = 'ie'
    ISRAEL = 'il'
    INDIA = 'in'
    ITALY = 'it'
    JAPAN = 'jp'
    SOUTH_KOREA = 'kr'
    LITHUANIA = 'lt'
    LATVIA = 'lv'
    MOROCCO = 'ma'
    MEXICO = 'mx'
    MALAYSIA = 'my'
    NIGERIA = 'ng'
    NETHERLANDS = 'nl'
    NORWAY = 'no'
    NEW_ZEALAND = 'nz'
    PHILIPPINES = 'ph'
    POLAND = 'pl'
    PORTUGAL = 'pt'
    ROMANIA = 'ro'
    SERBIA = 'rs'
    RUSSIA = 'ru'
    SAUDI_ARABIA = 'sa'
    SWEDEN = 'se'
    SINGAPORE = 'sg'
    SLOVENIA = 'si'
    SLOVAKIA = 'sk'
    THAILAND = 'th'
    TURKEY = 'tr'
    TAIWAN = 'tw'
    UKRAINE = 'ua'
    USA = 'us'
    VENEZUELA = 've'
    SOUTH_AFRICA = 'za'
