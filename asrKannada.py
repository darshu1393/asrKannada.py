#!/usr/bin/python3

import sys
import regex as re
import Text2TranscriptCleaner

class KnLangDatabase(Text2TranscriptCleaner.Text2TranscriptCleaner):

    def __init__(self, lang):
        super(KnLangDatabase, self).__init__()
        self.lang = lang
        # nt = 'nineteen 'F
        # et = 'eighteen '
        # st = 'seventeen '
        #  ನೇ = 'order '
        self.decades = {'1ನೇ':'ಒಂದುನೇ','2ನೇ':'ಎರಡನೇ','3ನೇ':'     ಮೂರನೇ','4ನೇ':'ನಾಲ್ಕನೇ','5ನೇ':'ಐದನೇ','6ನೇ':'ಆರನೇ','7ನೇ':'ಏಳುನೇ','8ನೇ':'ಎಂಟನೇ','9ನೇ':'ಒಂಬತ್ತನೇ','10ನೇ':'ಹತ್ತನೇ',
                        '11ನೇ':'ಹನ್ನೊಂದನೇ','12ನೇ':'ಹನ್ನೆರಡನೇ','13ನೇ':'ಹದಿಮೂರುನೇ','14ನೇ':'ಹದಿನಾಲ್ಕುನೇ','15ನೇ':'ಹದಿನೈದನೇ','16ನೇ':'ಹದಿನಾರುನೇ','17ನೇ':'ಹದಿನೇಳುನೇ','18ನೇ':'ಹದಿನೆಂಟುನೇ','19ನೇ':'ಹತ್ತೊಂಬತ್ತುನೇ','20ನೇ': 'ಇಪ್ಪತ್ತುನೇ',
                        '21ನೇ':'ಇಪ್ಪತ್ತೊಂದುನೇ','22ನೇ':'ಇಪ್ಪತ್ತೆರಡುನೇ','23ನೇ':'ಇಪ್ಪತ್ತ ಮೂರುನೇ','24ನೇ':'ಇಪ್ಪತ್ತುನಾಲ್ಕುನೇ','25ನೇ':'ಇಪ್ಪತ್ತೈದುನೇ','26ನೇ':'ಇಪ್ಪತ್ತಾರುನೇ','27ನೇ':'ಇಪ್ಪತ್ತು ಏಳುನೇ','28ನೇ':'ಇಪ್ಪತ್ತು ಎಂಟುನೇ','29ನೇ':'ಇಪ್ಪತ್ತೊಂಭತ್ತುನೇ','30ನೇ': 'ಮೂವತ್ತುನೇ',
                        '40ನೇ': 'ನಲವತ್ತನೇ', '50ನೇ': 'ಐವತ್ತುನೇ', '60ನೇ': 'ಅರವತ್ತುನೇ',
                        '70ನೇ': ' ಎಪ್ಪತ್ತುನೇ', '80ನೇ': 'ಎಂಭತ್ತುನೇ', '90ನೇ': 'ತೊಂಬತ್ತುನೇ', '100ನೇ':'ನೂರುನೇ','1000ನೇ':'ಸಾವಿರನೇ'
                        #'1710ನೇ': , '1720ನೇ': , '1730ನೇ': st+'thirties',
                        #'1740ನೇ': st+'fourties', '1750ನೇ': st+'fifties', '1760ನೇ': st+'sixties',
                        #'1770ನೇ': st+'seventies', '1780ನೇ': st+'eighties', '1790ನೇ': st+'nineties',
                        #'1810ನೇ': et+'tens', '1820ನೇ': et+'twenties', '1830ನೇ': et+'thirties',

                        #'1840ನೇ': et+'fourties', '1850ನೇ': et+'fifties', '1860ನೇ': et+'sixties',
                        #'1870ನೇ': et+'seventies', '1880ನೇ': et+'eighties', '1890ನೇ': et+'nineties',
                        #'1910ನೇ': nt+'tens', '1920ನೇ': nt+'twenties', '1930ನೇ': nt+'thirties',
                        #'1940ನೇ': nt+'fourties', '1950ನೇ': nt+'fifties', '1960ನೇ': nt+'sixties',
                        #'1970ನೇ': nt+'seventies', '1980ನೇ': nt+'eighties', '1990ನೇ': nt+'nineties',
                        #'1600ನೇ': 'sixteen hundreds', '1700ನೇ': st+'hundreds', '1800ನೇ': et+'hundreds', '1900ನೇ': nt+'hundreds',
                        #'2000ನೇ': 'two thousands'
        }

        self.centuries = {'1ನೇ':'ಒಂದುನೇ','2ನೇ':'ಎರಡನೇ','3ನೇ':' ಮೂರನೇ','4ನೇ':'ನಾಲ್ಕನೇ','5ನೇ':'ಐದನೇ','6ನೇ':'ಆರನೇ','7ನೇ':'ಏಳುನೇ','8ನೇ':'ಎಂಟನೇ','9ನೇ':'ಒಂಬತ್ತನೇ','10ನೇ':'ಹತ್ತನೇ',
                        '11ನೇ':'ಹನ್ನೊಂದನೇ','12ನೇ':'ಹನ್ನೆರಡನೇ','13ನೇ':'ಹದಿಮೂರುನೇ','14ನೇ':'ಹದಿನಾಲ್ಕುನೇ','15ನೇ':'ಹದಿನೈದನೇ','16ನೇ':'ಹದಿನಾರುನೇ','17ನೇ':'ಹದಿನೇಳುನೇ','18ನೇ':'ಹದಿನೆಂಟುನೇ','19ನೇ':'ಹತ್ತೊಂಬತ್ತುನೇ','20ನೇ': 'ಇಪ್ಪತ್ತುನೇ',
                        '21ನೇ':'ಇಪ್ಪತ್ತೊಂದುನೇ','22ನೇ':'ಇಪ್ಪತ್ತೆರಡುನೇ','23ನೇ':'ಇಪ್ಪತ್ತ ಮೂರುನೇ','24ನೇ':'ಇಪ್ಪತ್ತುನಾಲ್ಕುನೇ','25ನೇ':'ಇಪ್ಪತ್ತೈದುನೇ','26ನೇ':'ಇಪ್ಪತ್ತಾರುನೇ','27ನೇ':'ಇಪ್ಪತ್ತು ಏಳುನೇ','28ನೇ':'ಇಪ್ಪತ್ತು ಎಂಟುನೇ','29ನೇ':'ಇಪ್ಪತ್ತೊಂಭತ್ತುನೇ','30ನೇ': 'ಮೂವತ್ತುನೇ',
                        '40ನೇ': 'ನಲವತ್ತನೇ', '50ನೇ': 'ಐವತ್ತುನೇ', '60ನೇ': 'ಅರವತ್ತುನೇ',
                        '70ನೇ': ' ಎಪ್ಪತ್ತುನೇ', '80ನೇ': 'ಎಂಭತ್ತುನೇ', '90ನೇ': 'ತೊಂಬತ್ತುನೇ', '100ನೇ':'ನೂರುನೇ','1000ನೇ':'ಸಾವಿರನೇ'}

        lc_letters = "ಅಆಇಈಉಊಋಎಏಐಒಓಔಅಂಅಃಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲವಶಷಸಹಳೞಕಕಾಕಿಕೀಕುಕೂಕೃಕೆಕೇಕೈಕೊಕೋಕೌಕಂಕಃಖಖಾಖಿಖೀಖುಖೂಖೃಖೆಖೇಖೈಖೊಖೋಖೌಖಂಖಃಗಗಾಗಿಗೀಗುಗೂಗೃಗೆಗೇಗೈಗೊಗೋಗೌಗಂಗಃಘಘಾಘಿಘೀಘುಘೂಘೃಘೆಘೇಘೈಘೊಘೋಘೌಘಂಘಃಙಙಾಙಿಙೀಙುಙೂಙೃಙೆಙೇಙೈಙೊಙೋಙೌಙಂಙಚಚಾಚಿಚೀಚುಚೂಚೃಚೆಚೇಚೈಚೊಚೋಚೌಚಂಚಃಛಛಾಛಿಛೀಛುಛೂಛೃಛೆಛೇಛೈಛೊಛೋಛೌಛಂಛಃ ಜಜಾಜಿಜೀಜುಜೂಜೃಜೆಜೇಜೈಜೊಜೋಜೌಜಂಜಃಝಝಾಝಿಝೀಝುಝೂಝೃಝೆಝೇಝೈಝೊಝೋಝೌಝಂಝಃಞಞಾಞಿಞೀಞುಞೂಞೃಞೆಞೇಞೈಞೊಞೋಞೌಞಂಞಃಟಟಾಟಿಟೀಟುಟೂಟೃಟೆಟೇಟೈಟೊಟೋಟೌಟಂಟಃ ಠಠಾಠಿಠೀಠುಠೂಠೃಠೆಠೇಠೈಠೊಠೋಠೌಠಂಠಃಡಡಾಡಿಡೀಡುಡೂಡೃಡೆಡೇಡೈಡೊಡೋಡೌಡಂಡಃಢಢಾಢಿಢೀಢುಢೂಢೃಢೆಢೇಢೈಢೊಢೋಢೌಢಂಢಃಣಣಾಣಿಣೀಣುಣೂಣೃಣೆಣೇಣೈಣೊಣೋಣೌಣಂಣಃತತಾತಿತೀತುತೂತೃತೆತೇತೈತೊತೋತೌತಂತಃಥಥಾಥಿಥೀಥುಥೂಥೃಥೆಥೇಥೈಥೊಥೋಥೌಥಂಥಃದದಾದಿದೀದುದೂದೃದೆದೇದೈದೊದೋದೌದಂದಃಧಧಾಧಿಧೀಧುಧೂಧೃಧೆಧೇಧೈಧೊಧೋಧೌಧಂಧಃನನಾನಿನೀನುನೂನೃನೆನೇನೈನೊನೋನೌನಂನಃಪಪಾಪಿಪೀಪುಪೂಪೃಪೆಪೇಪೈಪೊಪೋಪೌಪಂಪಃಫಫಾಫಿಫೀಫುಫೂಫೃಫೆಫೇಫೈಫೊಫೋಫೌಫಂಫಃಬಬಾಬಿಬೀಬುಬೂಬೃಬೆಬೇಬೈಬೊಬೋಬೌಬಂಬಃಭಭಾಭಿಭೀಭುಭೂಭೃಭೆಭೇಭೈಭೊಭೋಭೌಭಂಭಃಮಮಾಮಿಮೀಮುಮೂಮೃಮೆಮೇಮೈಮೊಮೋಮೌಮಂಮಃಯಯಾಯಿಯೀಯುಯೂಯೃಯೆಯೇಯೈಯೊಯೋಯೌಯಂಯಃರರಾರಿರೀರುರೂರೃರೆರೇರೈರೊರೋರೌರಂರಃಱಱಾಱಿಱೀಱುಱೂಱೃಱೆಱೇಱೈಱೊಱೋಱೌಱಂಱಃಲಲಾಲಿಲೀಲುಲೂಲೃಲೆಲೇಲೈಲೊಲೋಲೌಲಂಲಃವವಾವಿವೀವುವೂವೃವೆವೇವೈವೊವೋವೌವಂವಃಶಶಾಶಿಶೀಶುಶೂಶೃಶೆಶೇಶೈಶೊಶೋಶೌಶಂಶಃಷಷಾಷಿಷೀಷುಷೂಷೃಷೆಷೇಷೈಷೊಷೋಷೌಷಂಷಃಸಸಾಸಿಸೀಸುಸೂಸೃಸೆಸೇಸೈಸೊಸೋಸೌಸಂಸಃಹಹಾಹಿಹೀಹುಹೂಹೃಹೆಹೇಹೈಹೊಹೋಹೌಹಂಹಃಳಳಾಳಿಳೀಳುಳೂಳೃಳೆಳೇಳೈಳೊಳೋಳೌಳಂಳಃೞೞಾೞಿೞೀೞುೞೂೞೃೞೆೞೇೞೈೞೊೞೋೞೌೞಂೞಃ"
        extra_letters = "ಕ್ ಖ್ ಗ್ ಘ್ ಙ್ ಚ್ ಛ್ ಜ್ ಝ್ ಞ್ ಟ್ ಠ್ ಡ್ ಢ್ ಣ್ ತ್ ಥ್ ದ್ ಧ್ ನ್ ಪ್ ಫ್ ಬ್ ಭ್ ಮ್ ಯ್ ರ್ ಱ್ ಲ್ ವ್ ಶ್ ಷ್ ಸ್ ಹ್ ಳ್ ೞ್ ಕ್ಕ ಖ್ಖ ಗ್ಗ ಚ್ಚ ಟ್ಟ ತ್ತ ತ್ರ ಧ್ಯ ದ್ದ ನ್ನ ಬ್ಬ ಮ್ಮ ರ್ತ ಲ್ಲ ಳ್ಳ ಸ್ಥ ಸ್ಪ ಸ್ವ ಹ್ಹ ಸ್ಥಾ ೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯"
        #self.roman_pat = '^[XIVMLDC]{2,}$'
        
        latin_letters = "\p{Latin}"
        self.word_pat = "^[ \'" + lc_letters + extra_letters + latin_letters + "]+$" # including space

        # set first elem to None if not implemented in num2words
        self.currency_symbols = {'र₹':('INR','ರೂಪಾಯಿ'), '£': ('GBP','ಪೌಂಡ್ಸ್'), '$': ('USD', 'ಡಾಲರ್'), '€': ('EUR','ಯುರೋ'), '¥': (None, 'ಯಾವುದೂ')}
        self.currencies = "[" + "".join(self.currency_symbols.keys()) + "]"

        self.special_symbols = {'°': 'ಡಿಗ್ರಿ', '˚': 'ಡಿಗ್ರಿ', '/': 'ವಿಭಾಗ', '&': 'ಮತ್ತು', '+': 'ಕುಡಿಸು', '=': 'ಸಮಾನ',
                                '%': 'ಶೇಕಡ', '^': 'ಕೆರೆಟ್', '#': 'ಸಂಖ್ಯೆ ', '№': 'ಸಂಖ್ಯೆ',
                                # 'mon': 'Monday', 'tue': 'Tuesday', 'tues': 'Tuesday', 'wed': 'Wednesday', 'thu': 'Thursday',
                                #'thurs': 'Thursday', 'fri': 'Friday',
                                #'feb': 'February', 'mar': 'March', 'apr': 'April', 'jun': 'June',
                                #'jul': 'July', 'aug': 'August', 'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December',
                                # length units
                                'ಕಿ.ಮೀ': 'ಕಿಲೋಮೀಟರ್','ಎಂಎಂ': 'ಮಿಲ್ಲಿ ಮೀಟರ್','ft': 'ಅಡಿ', 'ಮೈಲಿ.':'ಮೈಲಿಗಳು', 'yd': 'ಗಜ',
                                'ಸಿ.ಎಂ': 'ಸೆಂಟಿಮೀಟರ್ಗಳು', 'ಡಿ.ಎಂ': 'ಡೆಸಿಮೀಟರ್ಗಳು', 'nm': 'ನಾನೋ ಮೀಟರ್ಗಳು', 'µ': 'ಮೈಕ್ರನ್ಸ್' ,
                                 # weight units
                                'lb': 'ಪೌಂಡ್', 'lbs': 'ಪೌಂಡ್ಸ್', 'ಮಿ.ಗ್ರಾಂ.': 'ಮಿಲ್ಲಿ ಗ್ರಾಂಗಳು', 'ಸಿ.ಗ್ರಾಂ.': 'ಸೆಂಟಿಗ್ರಾಮ್ಗಳು', 'ಗ್ರಾಂ.': 'ಗ್ರಾಂಗಳು',
                                'ಕೆ.ಗ್ರಾಂ.': 'ಕಿಲೋಗ್ರಾಂ', 'ಕ್ಯಾ.': 'ಕ್ಯಾರೆಟ್',
                                # electricity and power units
                                'hz': 'ಹರ್ಟ್ಜ್', 'khz': 'ಕಿಲೊ ಹೆರ್ಟ್ಜ್', 'mhz': 'ಮೆಗಾ ಹರ್ಟ್ಜ್', 'mw': 'ಮಿಲಿ ವ್ಯಾಟ್',
                                'kw': 'ಕಿಲೊ ವ್ಯಾಟ್', 'mv': 'ಮಿಲಿ ವೋಲ್ಟ್', 'kv': 'ಕಿಲೊ ವೋಲ್ಟ್',
                                # time units
                                'ns': 'ನ್ಯಾನೋ ಸೆಕೆಂಡುಗಳು', 'ms': 'ಮಿಲಿ ಸೆಕೆಂಡುಗಳು',
                                # volume units
                                'qt': 'ಕ್ವಾರ್ಟರ್ಸ್', 'ml': 'ಮಿಲಿಲೀಟರ್ಗಳು', 'cl': 'సెಸೆಂಟಿಲೈಟರ್ಸ್', 'dl': 'ಡೆಸಿಲೀಟರ್',
                                'hl': 'ಹೆಕ್ಟ ಲೀಟರ್', 'kl': 'ಕಿಲೋ ಲೀಟರ್',
                                # speed units
                                'mph': 'ಗಂಟೆಗೆ ಮೈಲುಗಳು ', 'kmh': 'ಗಂಟೆಗೆ ಕಿಲೋಮೀಟರ್',
                                # bytes
                                'kb': 'ಕಿಲೋಬೈಟ್ಗಳು ', 'mb': 'ಮೆಗಾಬೈಟ್ಗಳು', 'gb': 'ಗಿಗಾ ಬೈಟ್ಸ್', 'tb': 'ತೆರೆ ಬೈಟ್ಸ್ ',
                                # other units
                                'lm': 'ಲ್ಯುಮೆನ್ಸ್','cd':'ಮೇಣದಬತ್ತಿಗಳು', 'hg': 'ಪಾದರಸದ'}

        self.special_symbols_before_num = {'ಕ್ರಿ.ಶ':'ಕ್ರಿಸ್ತನ ಯುಗ','ಕ್ರಿ.ಪೂ':'ಕ್ರಿಸ್ತ ಪೂರ್ವ'}
        self.special_symbols_after_num = {'m': 'ಮೀಟರ್ಗಳು', 'in': 'ಇಂಚುಗಳು', 'ha': 'ಹೆಕ್ಟೇರ್ಗಳು ',
                                          'l': 'ಲೀಟರ್ ', 'pa': 'ಪ್ಯಾಸ್ಕಲ್ಸ್', 'oz': 'ಔನ್ಸ್', 'g': 'ಗ್ರಮ್ಸ್',
                                          't': 'ಟನ್ಗಳು', 'gal': 'ಗಲಾನ್ಸ್', 'min': 'ನಿಮಿಷಗಳು', 'h': 'ಗಂಟೆಗಳ', 's': 'ಸೆಕೆಂಡುಗಳು',
                                          'w': 'ವಾಟ್ಸ್', 'v': 'ವೋಲ್ಟುಗಳು', 'ma': 'ಮಿಲ್ಲಿ ಆಂಪಿಯರ್ಗಳು '} # 'a': 'amperes' is too ambiguous even after numbers
        self.m_units = "|".join(self.special_symbols_after_num.keys())
        self.special_symbols_after_num.update(self.special_symbols)

        self.abbr  = "Mr|Mr?s|[M]iss|Drs?|Profs?|Sens?|Reps?|Attys?|Lt|Col|Gen|Messrs|Govs?|Adm|Rev|Maj|Sgt|Cpl|Pvt|Capt"
        self.abbr += "|Ste?|Ave|Pres|Lieut|Hon|Brig|Co?mdr|Pfc|Spc|Supts?|Det|Mt|Ft|Adj|Adv|Asst|Assoc|Ens|Insp|Mlle|Mme|Msgr|Sfc"
        self.abbr += "|Invt|Elec|Natl|M[ft]g"
        self.abbr += "|vs|Alex|Wm|Jos|Cie|fl|[o]z|TREAS|Ph"
        self.abbr += "|figs?|prop|nos?|art|bldg|prop"
        self.abbr += "|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec"
        self.abbr += "|Mon|Tue|Tues|Wed|Thu|Thurs|Fri"
        self.abbr += "|Ala|Ariz|[A]z|[A]rk|Calif|Colo|Conn|Ct|Dak|Del|Fla|Ga|[I]ll|Ind|Kans?|Ky"
        self.abbr += "|La|[M]ass|Md|Mich|Minn|[M]iss|Mo|Mont|Neb|Nev|Okla|[O]re|Pa|Penn|Tenn|Tex|Va|Vt|[W]ash|Wisc?|Wyo"
        self.abbr += "|Inc|Cos?|Corp|Pp?t[ye]s?|Ltd|Plc|Rt|Bancorp|Dept|Bhd|Assn|Univ|Intl|Sys"
        self.abbr += "|tel|est|ext|se?q|Jr|Sr|Bros|(Ed|Ph)\.D|Blvd|Rd|Esq|"
        self.abbr += "|".join([ re.escape(x) for x in self.special_symbols.keys() ])

        # The following is for handling e-mail addresses, use single spaces around words, please:
        self.at = 'ಸೈನ್ ಇನ್ '
        self.dot = ' ಡಾಟ್ '
        self.hyphen = 'ಡ್ಯಾಶ್ '
        self.underscore = 'ಅಂಡರ್ ಸ್ಕರ್ '

    def before_tokenize_lang(self, line):
        out = ' ' + line + ' '
        out = re.sub(r'(mm|cm|m|ft|in|km|mi)[2²]', r' \1 squared ', out)
        out = re.sub(r' fl\.? oz\b', 'fluid ounces ', out)
         # hashtag
        out = re.sub(r'#([a-z][a-z0-9]+)', r' hashtag \1 ', out)
        out = re.sub(r'°[Cc]', ' degrees centigrade ', out)
        out = re.sub(r'°[Ff]', ' degrees fahrenheit ', out)

        return out[1:len(out)-1]

    def after_tokenize_lang(self, line):
        out = ' ' + line + ' '
        # split numbers separated by a hyphen:
        out = re.sub(r'(\d+)[–\-](\d+)', r'\1 \2', out)
        # attach back the apostrophes:
        out = re.sub(r'n \' t', r"n't", out)
        out = re.sub(r'(\p{L}) ?[´\'´`ʼʻ] ?s', r"\1's", out) # NOTE: no space here before 's , it remains attached. Change this is necessary
        out = re.sub(r'(\p{L}s) ?[´\'´`ʼʻ] ', r"\1' ", out) # NOTE: plural possesive apostrophe remains attached. Maybe change to s'' and detach if necessary.
        out = re.sub(r'(\w) \' (re|ve|ll|d|m)', r"\1'\2", out)
        out = re.sub(r"(\d+) ?' ?(\d+) \"", r"\1 feet \2 inches", out)
        out = re.sub('e \- mail', 'email', out)

        return out[1:len(out)-1]

    def ifOrdinal(self, w):
        return re.search("^(th|st|nd|rd)$", w) # NOTE: just the abbrevs here, not the number

    def preprocess_number(self, w):
        out = w
        out = re.sub(r'[,](\d\d\d)', r'\1', out)
        out = re.sub(r'[.,]00$', '', out)
        out = re.sub(r'[,](\d\d?)$', r'.\1', out)
        if len(out):
            return out
        return w
