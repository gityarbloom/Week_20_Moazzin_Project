


class RiskLevelAnalysis:

    def __init__(self, h_level: str, l_level: str):
        self.h_level = self.smart_division_to_sections(h_level)
        self.l_level = self.smart_division_to_sections(l_level)
        self.percent_bds = None
        self.is_bds = None
        self.level_threat_bds = None


    def smart_division_to_sections(self, words_string: str):
        if words_string.count(",") > len(words_string) / 20:
            return words_string.lower().split(",")
        else:
            return words_string.lower().split(" ")
        

    def get_percent_bds(self, text: str):
        if self.percent_bds is None:
            sum_danger = 0
            for word in text:
                if word in self.l_level:
                    sum_danger += len(text) / 20
                elif word in self.h_level:
                    sum_danger += len(text) / 10
                if sum_danger >= 100:
                    self.percent_bds = 100
                    return self.percent_bds
            self.percent_bds = sum_danger
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
    

    def restart_analyser(self):
        self.percent_bds = None
        self.is_bds = None
        self.level_threat_bds = None