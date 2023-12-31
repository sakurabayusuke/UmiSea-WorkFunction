from marshmallow import Schema, fields, post_load


class FiledAliases:
    def __init__(self, 海底地形名, かな, Undersea_Feature_Name, 属名, 水深, 呼称の由来, 由来_En, 会議名, JCUFN_approved, SCUFN_approved):
        self.海底地形名 = 海底地形名
        self.かな = かな
        self.Undersea_Feature_Name = Undersea_Feature_Name
        self.属名 = 属名
        self.水深 = 水深
        self.呼称の由来 = 呼称の由来
        self.由来_En = 由来_En
        self.会議名 = 会議名
        self.JCUFN_approved = JCUFN_approved
        self.SCUFN_approved = SCUFN_approved


class FiledAliasesSchema(Schema):
    海底地形名 = fields.Str()
    かな = fields.Str()
    Undersea_Feature_Name = fields.Str()
    属名 = fields.Str()
    水深 = fields.Str()
    呼称の由来 = fields.Str()
    由来_En = fields.Str()
    会議名 = fields.Str()
    JCUFN_approved = fields.Str()
    SCUFN_approved = fields.Str()

    @post_load
    def make_filed_aliases(self, data, **kwargs):
        return FiledAliases(**data)
