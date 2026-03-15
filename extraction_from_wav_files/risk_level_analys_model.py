class RiskLevelAnalysis:

    def __init__(self, h_level: str, l_level: str):
        self.h_level = self.smart_division_to_sections(h_level)
        self.l_level = self.smart_division_to_sections(l_level)
        self.percent_bds = None
        self.is_bds = None
        self.level_threat_bds = None


    def smart_division_to_sections(self, words_string: str):
        if words_string.count(",") > len(words_string) / 20:
            words_string = words_string.lower().split(",")
            for i in range(len(words_string)):
                words_string[i] = words_string[i].split()
            return words_string
        else:
            return words_string.lower().split(" ")
        

    def get_percent_bds(self, text: str):
        if self.percent_bds is None:
            text = self.smart_division_to_sections(text)
            risk_count = 0

            for i in range(len(text)):
                if self.couples_check(text, i, self.l_level):
                    risk_count += len(text) / 20
                elif self.couples_check(text, i, self.h_level):
                    risk_count += len(text) / 10
                if risk_count >= 100:
                    self.percent_bds = 100
                    return self.percent_bds
            self.percent_bds = risk_count
        return self.percent_bds
    

    def is_it_bds(self, text: str):
        if self.is_bds is None:
            self.is_bds = self.get_percent_bds(text=text) >= 30
        return self.is_bds
    

    def get_level_threat_bds(self, text: str):
        if self.level_threat_bds is None:
            if self.get_percent_bds(text=text) < 30:
                self.level_threat_bds = "none"
            elif self.get_percent_bds(text=text) < 70:
                self.level_threat_bds = "medium"
            else:
                self.level_threat_bds = "high"
        return self.level_threat_bds
    

    def couples_check(self, text: list[str], index: int, check_list: list):
        for x in check_list:
            if text[index] in x:
                if len(x) == 1:
                    return True
                if index < len(text) -1 and text[index +1] == x[1]:
                    return True
        return False
    
    
    def restart_analyser(self):
        self.percent_bds = None
        self.is_bds = None
        self.level_threat_bds = None