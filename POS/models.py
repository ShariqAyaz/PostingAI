from django.db import models


class Accountscreenvalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accountscreenid = models.ForeignKey('Accountscreens', models.DO_NOTHING, db_column='AccountScreenId')  # Field name made lowercase.
    accounttypeid = models.IntegerField(db_column='AccountTypeId')  # Field name made lowercase.
    accounttypename = models.TextField(db_column='AccountTypeName', blank=True, null=True)  # Field name made lowercase.
    displaydetails = models.BooleanField(db_column='DisplayDetails')  # Field name made lowercase.
    hidezerobalanceaccounts = models.BooleanField(db_column='HideZeroBalanceAccounts')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountScreenValues'
        unique_together = (('id', 'accountscreenid'),)


class Accountscreens(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    filter = models.IntegerField(db_column='Filter')  # Field name made lowercase.
    displayastree = models.BooleanField(db_column='DisplayAsTree')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    automationcommandmapdata = models.TextField(db_column='AutomationCommandMapData', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountScreens'


class Accounttransactiondocumentaccountmaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accounttransactiondocumenttypeid = models.ForeignKey('Accounttransactiondocumenttypes', models.DO_NOTHING, db_column='AccountTransactionDocumentTypeId')  # Field name made lowercase.
    accountid = models.IntegerField(db_column='AccountId')  # Field name made lowercase.
    accountname = models.TextField(db_column='AccountName', blank=True, null=True)  # Field name made lowercase.
    mappedaccountid = models.IntegerField(db_column='MappedAccountId')  # Field name made lowercase.
    mappedaccountname = models.TextField(db_column='MappedAccountName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountTransactionDocumentAccountMaps'


class Accounttransactiondocumenttypeaccounttransactiontypes(models.Model):
    accounttransactiondocumenttype = models.OneToOneField('Accounttransactiondocumenttypes', models.DO_NOTHING, db_column='AccountTransactionDocumentType_Id', primary_key=True)  # Field name made lowercase.
    accounttransactiontype = models.ForeignKey('Accounttransactiontypes', models.DO_NOTHING, db_column='AccountTransactionType_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountTransactionDocumentTypeAccountTransactionTypes'
        unique_together = (('accounttransactiondocumenttype', 'accounttransactiontype'),)


class Accounttransactiondocumenttypemaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accounttransactiondocumenttypeid = models.ForeignKey('Accounttransactiondocumenttypes', models.DO_NOTHING, db_column='AccountTransactionDocumentTypeId')  # Field name made lowercase.
    terminalid = models.IntegerField(db_column='TerminalId')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountTransactionDocumentTypeMaps'


class Accounttransactiondocumenttypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    buttonheader = models.TextField(db_column='ButtonHeader', blank=True, null=True)  # Field name made lowercase.
    buttoncolor = models.TextField(db_column='ButtonColor', blank=True, null=True)  # Field name made lowercase.
    masteraccounttypeid = models.IntegerField(db_column='MasterAccountTypeId')  # Field name made lowercase.
    defaultamount = models.TextField(db_column='DefaultAmount', blank=True, null=True)  # Field name made lowercase.
    descriptiontemplate = models.TextField(db_column='DescriptionTemplate', blank=True, null=True)  # Field name made lowercase.
    exchangetemplate = models.TextField(db_column='ExchangeTemplate', blank=True, null=True)  # Field name made lowercase.
    batchcreatedocuments = models.BooleanField(db_column='BatchCreateDocuments')  # Field name made lowercase.
    filter = models.IntegerField(db_column='Filter')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    printertemplateid = models.IntegerField(db_column='PrinterTemplateId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountTransactionDocumentTypes'


class Accounttransactiondocuments(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    documenttypeid = models.IntegerField(db_column='DocumentTypeId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountTransactionDocuments'


class Accounttransactiontypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    sourceaccounttypeid = models.IntegerField(db_column='SourceAccountTypeId')  # Field name made lowercase.
    targetaccounttypeid = models.IntegerField(db_column='TargetAccountTypeId')  # Field name made lowercase.
    defaultsourceaccountid = models.IntegerField(db_column='DefaultSourceAccountId')  # Field name made lowercase.
    defaulttargetaccountid = models.IntegerField(db_column='DefaultTargetAccountId')  # Field name made lowercase.
    foreigncurrencyid = models.IntegerField(db_column='ForeignCurrencyId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountTransactionTypes'


class Accounttransactionvalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accounttransactionid = models.ForeignKey('Accounttransactions', models.DO_NOTHING, db_column='AccountTransactionId',related_name='accounttransactionid_accounttransactionvalues')  # Field name made lowercase.
    accounttransactiondocumentid = models.ForeignKey('Accounttransactions', models.DO_NOTHING, db_column='AccountTransactionDocumentId',related_name='accounttransactiondocumentid_accounttransactionvalues')  # Field name made lowercase.
    accounttypeid = models.IntegerField(db_column='AccountTypeId')  # Field name made lowercase.
    accountid = models.IntegerField(db_column='AccountId')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    debit = models.DecimalField(db_column='Debit', max_digits=16, decimal_places=2)  # Field name made lowercase.
    credit = models.DecimalField(db_column='Credit', max_digits=16, decimal_places=2)  # Field name made lowercase.
    exchange = models.DecimalField(db_column='Exchange', max_digits=16, decimal_places=2)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountTransactionValues'
        unique_together = (('id', 'accounttransactionid', 'accounttransactiondocumentid'),)


class Accounttransactions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accounttransactiondocumentid = models.ForeignKey(Accounttransactiondocuments, models.DO_NOTHING, db_column='AccountTransactionDocumentId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=16, decimal_places=2)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=16, decimal_places=2)  # Field name made lowercase.
    accounttransactiontypeid = models.IntegerField(db_column='AccountTransactionTypeId')  # Field name made lowercase.
    sourceaccounttypeid = models.IntegerField(db_column='SourceAccountTypeId')  # Field name made lowercase.
    targetaccounttypeid = models.IntegerField(db_column='TargetAccountTypeId')  # Field name made lowercase.
    isreversed = models.BooleanField(db_column='IsReversed')  # Field name made lowercase.
    reversable = models.BooleanField(db_column='Reversable')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountTransactions'
        unique_together = (('id', 'accounttransactiondocumentid'),)


class Accounttypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    defaultfiltertype = models.IntegerField(db_column='DefaultFilterType')  # Field name made lowercase.
    workingrule = models.IntegerField(db_column='WorkingRule')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    tags = models.TextField(db_column='Tags', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountTypes'


class Accounts(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accounttypeid = models.IntegerField(db_column='AccountTypeId')  # Field name made lowercase.
    foreigncurrencyid = models.IntegerField(db_column='ForeignCurrencyId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Accounts'


class Actioncontainers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    appactionid = models.IntegerField(db_column='AppActionId')  # Field name made lowercase.
    appruleid = models.ForeignKey('Apprules', models.DO_NOTHING, db_column='AppRuleId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    parametervalues = models.TextField(db_column='ParameterValues', blank=True, null=True)  # Field name made lowercase.
    customconstraint = models.TextField(db_column='CustomConstraint', blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActionContainers'


class Appactions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    actiontype = models.TextField(db_column='ActionType', blank=True, null=True)  # Field name made lowercase.
    parameter = models.TextField(db_column='Parameter', blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AppActions'


class Apprulemaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    appruleid = models.ForeignKey('Apprules', models.DO_NOTHING, db_column='AppRuleId')  # Field name made lowercase.
    terminalid = models.IntegerField(db_column='TerminalId')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AppRuleMaps'


class Apprules(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    eventname = models.TextField(db_column='EventName', blank=True, null=True)  # Field name made lowercase.
    eventconstraints = models.TextField(db_column='EventConstraints', blank=True, null=True)  # Field name made lowercase.
    customconstraint = models.TextField(db_column='CustomConstraint', blank=True, null=True)  # Field name made lowercase.
    ruleconstraints = models.TextField(db_column='RuleConstraints', blank=True, null=True)  # Field name made lowercase.
    constraintmatch = models.IntegerField(db_column='ConstraintMatch')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AppRules'


class Automationcommandmaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    automationcommandid = models.ForeignKey('Automationcommands', models.DO_NOTHING, db_column='AutomationCommandId')  # Field name made lowercase.
    displayonticket = models.BooleanField(db_column='DisplayOnTicket')  # Field name made lowercase.
    displayonpayment = models.BooleanField(db_column='DisplayOnPayment')  # Field name made lowercase.
    displayonorders = models.BooleanField(db_column='DisplayOnOrders')  # Field name made lowercase.
    displayonticketlist = models.BooleanField(db_column='DisplayOnTicketList')  # Field name made lowercase.
    displayunderticket = models.BooleanField(db_column='DisplayUnderTicket')  # Field name made lowercase.
    displayunderticket2 = models.BooleanField(db_column='DisplayUnderTicket2')  # Field name made lowercase.
    displayoncommandselector = models.BooleanField(db_column='DisplayOnCommandSelector')  # Field name made lowercase.
    enabledstates = models.TextField(db_column='EnabledStates', blank=True, null=True)  # Field name made lowercase.
    visiblestates = models.TextField(db_column='VisibleStates', blank=True, null=True)  # Field name made lowercase.
    terminalid = models.IntegerField(db_column='TerminalId')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AutomationCommandMaps'


class Automationcommands(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    buttonheader = models.TextField(db_column='ButtonHeader', blank=True, null=True)  # Field name made lowercase.
    color = models.TextField(db_column='Color', blank=True, null=True)  # Field name made lowercase.
    fontsize = models.IntegerField(db_column='FontSize')  # Field name made lowercase.
    values = models.TextField(db_column='Values', blank=True, null=True)  # Field name made lowercase.
    togglevalues = models.BooleanField(db_column='ToggleValues')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AutomationCommands'


class Calculationselectorcalculationtypes(models.Model):
    calculationselector = models.OneToOneField('Calculationselectors', models.DO_NOTHING, db_column='CalculationSelector_Id', primary_key=True)  # Field name made lowercase.
    calculationtype = models.ForeignKey('Calculationtypes', models.DO_NOTHING, db_column='CalculationType_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalculationSelectorCalculationTypes'
        unique_together = (('calculationselector', 'calculationtype'),)


class Calculationselectormaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    calculationselectorid = models.ForeignKey('Calculationselectors', models.DO_NOTHING, db_column='CalculationSelectorId')  # Field name made lowercase.
    terminalid = models.IntegerField(db_column='TerminalId')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalculationSelectorMaps'


class Calculationselectors(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    buttonheader = models.TextField(db_column='ButtonHeader', blank=True, null=True)  # Field name made lowercase.
    buttoncolor = models.TextField(db_column='ButtonColor', blank=True, null=True)  # Field name made lowercase.
    fontsize = models.IntegerField(db_column='FontSize')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalculationSelectors'


class Calculationtypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    calculationmethod = models.IntegerField(db_column='CalculationMethod')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=16, decimal_places=2)  # Field name made lowercase.
    maxamount = models.DecimalField(db_column='MaxAmount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    includetax = models.BooleanField(db_column='IncludeTax')  # Field name made lowercase.
    decreaseamount = models.BooleanField(db_column='DecreaseAmount')  # Field name made lowercase.
    useplainsum = models.BooleanField(db_column='UsePlainSum')  # Field name made lowercase.
    togglecalculation = models.BooleanField(db_column='ToggleCalculation')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    accounttransactiontype = models.ForeignKey(Accounttransactiontypes, models.DO_NOTHING, db_column='AccountTransactionType_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalculationTypes'


class Calculations(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='TicketId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    order = models.IntegerField(db_column='Order')  # Field name made lowercase.
    calculationtypeid = models.IntegerField(db_column='CalculationTypeId')  # Field name made lowercase.
    accounttransactiontypeid = models.IntegerField(db_column='AccountTransactionTypeId')  # Field name made lowercase.
    calculationtype = models.IntegerField(db_column='CalculationType')  # Field name made lowercase.
    includetax = models.BooleanField(db_column='IncludeTax')  # Field name made lowercase.
    decreaseamount = models.BooleanField(db_column='DecreaseAmount')  # Field name made lowercase.
    useplainsum = models.BooleanField(db_column='UsePlainSum')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=16, decimal_places=2)  # Field name made lowercase.
    calculationamount = models.DecimalField(db_column='CalculationAmount', max_digits=16, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calculations'
        unique_together = (('id', 'ticketid'),)


class Changepaymenttypemaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    changepaymenttypeid = models.ForeignKey('Changepaymenttypes', models.DO_NOTHING, db_column='ChangePaymentTypeId')  # Field name made lowercase.
    terminalid = models.IntegerField(db_column='TerminalId')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChangePaymentTypeMaps'


class Changepaymenttypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    accounttransactiontype = models.ForeignKey(Accounttransactiontypes, models.DO_NOTHING, db_column='AccountTransactionType_Id', blank=True, null=True)  # Field name made lowercase.
    account = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='Account_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChangePaymentTypes'


class Changepayments(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='TicketId')  # Field name made lowercase.
    changepaymenttypeid = models.IntegerField(db_column='ChangePaymentTypeId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    accounttransactionid = models.IntegerField(db_column='AccountTransactionId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    accounttransaction = models.ForeignKey(Accounttransactions, models.DO_NOTHING, db_column='AccountTransaction_Id', blank=True, null=True,related_name='accounttransaction_changepayments_set')  # Field name made lowercase.
    accounttransaction_accounttransactiondocumentid = models.ForeignKey(Accounttransactions, models.DO_NOTHING, db_column='AccountTransaction_AccountTransactionDocumentId', blank=True, null=True,related_name='accounttransaction_accounttransactiondocumentid_changepayments_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChangePayments'
        unique_together = (('id', 'ticketid'),)


class Costitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    warehouseconsumptionid = models.ForeignKey('Warehouseconsumptions', models.DO_NOTHING, db_column='WarehouseConsumptionId',related_name='warehouseconsumptionid_costitems_set')  # Field name made lowercase.
    periodicconsumptionid = models.ForeignKey('Warehouseconsumptions', models.DO_NOTHING, db_column='PeriodicConsumptionId',related_name='periodicconsumptionid_costitems_set')  # Field name made lowercase.
    menuitemid = models.IntegerField(db_column='MenuItemId')  # Field name made lowercase.
    portionid = models.IntegerField(db_column='PortionId')  # Field name made lowercase.
    portionname = models.TextField(db_column='PortionName', blank=True, null=True)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=16, decimal_places=3)  # Field name made lowercase.
    costprediction = models.DecimalField(db_column='CostPrediction', max_digits=16, decimal_places=2)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=16, decimal_places=2)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CostItems'
        unique_together = (('id', 'warehouseconsumptionid', 'periodicconsumptionid'),)


class Departments(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    pricetag = models.CharField(db_column='PriceTag', max_length=10, blank=True, null=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WarehouseId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.
    screenmenuid = models.IntegerField(db_column='ScreenMenuId')  # Field name made lowercase.
    ticketcreationmethod = models.IntegerField(db_column='TicketCreationMethod')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Departments'


class Entities(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entitytypeid = models.IntegerField(db_column='EntityTypeId')  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='LastUpdateTime')  # Field name made lowercase.
    searchstring = models.TextField(db_column='SearchString', blank=True, null=True)  # Field name made lowercase.
    customdata = models.TextField(db_column='CustomData', blank=True, null=True)  # Field name made lowercase.
    accountid = models.IntegerField(db_column='AccountId')  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WarehouseId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Entities'


class Entitycustomfields(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    fieldtype = models.IntegerField(db_column='FieldType')  # Field name made lowercase.
    editingformat = models.TextField(db_column='EditingFormat', blank=True, null=True)  # Field name made lowercase.
    valuesource = models.TextField(db_column='ValueSource', blank=True, null=True)  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    entitytype = models.ForeignKey('Entitytypes', models.DO_NOTHING, db_column='EntityType_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EntityCustomFields'


class Entityscreenitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entityscreenid = models.ForeignKey('Entityscreens', models.DO_NOTHING, db_column='EntityScreenId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    entityid = models.IntegerField(db_column='EntityId')  # Field name made lowercase.
    entitystate = models.TextField(db_column='EntityState', blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='LastUpdateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EntityScreenItems'
        unique_together = (('id', 'entityscreenid'),)


class Entityscreenmaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entityscreenid = models.ForeignKey('Entityscreens', models.DO_NOTHING, db_column='EntityScreenId')  # Field name made lowercase.
    terminalid = models.IntegerField(db_column='TerminalId')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EntityScreenMaps'


class Entityscreens(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.
    entitytypeid = models.IntegerField(db_column='EntityTypeId')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    displaymode = models.IntegerField(db_column='DisplayMode')  # Field name made lowercase.
    backgroundcolor = models.TextField(db_column='BackgroundColor', blank=True, null=True)  # Field name made lowercase.
    backgroundimage = models.TextField(db_column='BackgroundImage', blank=True, null=True)  # Field name made lowercase.
    fontsize = models.IntegerField(db_column='FontSize')  # Field name made lowercase.
    pagecount = models.IntegerField(db_column='PageCount')  # Field name made lowercase.
    rowcount = models.IntegerField(db_column='RowCount')  # Field name made lowercase.
    columncount = models.IntegerField(db_column='ColumnCount')  # Field name made lowercase.
    buttonheight = models.IntegerField(db_column='ButtonHeight')  # Field name made lowercase.
    displaystate = models.TextField(db_column='DisplayState', blank=True, null=True)  # Field name made lowercase.
    statefilter = models.TextField(db_column='StateFilter', blank=True, null=True)  # Field name made lowercase.
    asktickettype = models.BooleanField(db_column='AskTicketType')  # Field name made lowercase.
    searchvaluereplacepattern = models.TextField(db_column='SearchValueReplacePattern', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EntityScreens'


class Entitystatevalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entityid = models.IntegerField(db_column='EntityId', unique=True)  # Field name made lowercase.
    entitystates = models.TextField(db_column='EntityStates', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EntityStateValues'


class Entitytypeassignments(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tickettypeid = models.ForeignKey('Tickettypes', models.DO_NOTHING, db_column='TicketTypeId')  # Field name made lowercase.
    entitytypeid = models.IntegerField(db_column='EntityTypeId')  # Field name made lowercase.
    entitytypename = models.TextField(db_column='EntityTypeName', blank=True, null=True)  # Field name made lowercase.
    askbeforecreatingticket = models.BooleanField(db_column='AskBeforeCreatingTicket')  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    copytonewtickets = models.BooleanField(db_column='CopyToNewTickets')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EntityTypeAssignments'
        unique_together = (('id', 'tickettypeid'),)


class Entitytypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    entityname = models.TextField(db_column='EntityName', blank=True, null=True)  # Field name made lowercase.
    accounttypeid = models.IntegerField(db_column='AccountTypeId')  # Field name made lowercase.
    warehousetypeid = models.IntegerField(db_column='WarehouseTypeId')  # Field name made lowercase.
    accountnametemplate = models.TextField(db_column='AccountNameTemplate', blank=True, null=True)  # Field name made lowercase.
    primaryfieldname = models.TextField(db_column='PrimaryFieldName', blank=True, null=True)  # Field name made lowercase.
    primaryfieldformat = models.TextField(db_column='PrimaryFieldFormat', blank=True, null=True)  # Field name made lowercase.
    displayformat = models.TextField(db_column='DisplayFormat', blank=True, null=True)  # Field name made lowercase.
    accountbalancedisplayformat = models.TextField(db_column='AccountBalanceDisplayFormat', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EntityTypes'


class Foreigncurrencies(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    currencysymbol = models.TextField(db_column='CurrencySymbol', blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=18, decimal_places=2)  # Field name made lowercase.
    rounding = models.DecimalField(db_column='Rounding', max_digits=18, decimal_places=2)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ForeignCurrencies'


class Inventoryitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    groupcode = models.TextField(db_column='GroupCode', blank=True, null=True)  # Field name made lowercase.
    baseunit = models.TextField(db_column='BaseUnit', blank=True, null=True)  # Field name made lowercase.
    transactionunit = models.TextField(db_column='TransactionUnit', blank=True, null=True)  # Field name made lowercase.
    transactionunitmultiplier = models.IntegerField(db_column='TransactionUnitMultiplier')  # Field name made lowercase.
    warehouse = models.TextField(db_column='Warehouse', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryItems'


class Inventorytransactiondocumenttypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sourceentitytypeid = models.IntegerField(db_column='SourceEntityTypeId')  # Field name made lowercase.
    targetentitytypeid = models.IntegerField(db_column='TargetEntityTypeId')  # Field name made lowercase.
    defaultsourceentityid = models.IntegerField(db_column='DefaultSourceEntityId')  # Field name made lowercase.
    defaulttargetentityid = models.IntegerField(db_column='DefaultTargetEntityId')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    accounttransactiontype = models.ForeignKey(Accounttransactiontypes, models.DO_NOTHING, db_column='AccountTransactionType_Id', blank=True, null=True)  # Field name made lowercase.
    inventorytransactiontype = models.ForeignKey('Inventorytransactiontypes', models.DO_NOTHING, db_column='InventoryTransactionType_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryTransactionDocumentTypes'


class Inventorytransactiondocuments(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryTransactionDocuments'


class Inventorytransactiontypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sourcewarehousetypeid = models.IntegerField(db_column='SourceWarehouseTypeId')  # Field name made lowercase.
    targetwarehousetypeid = models.IntegerField(db_column='TargetWarehouseTypeId')  # Field name made lowercase.
    defaultsourcewarehouseid = models.IntegerField(db_column='DefaultSourceWarehouseId')  # Field name made lowercase.
    defaulttargetwarehouseid = models.IntegerField(db_column='DefaultTargetWarehouseId')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryTransactionTypes'


class Inventorytransactions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    inventorytransactiondocumentid = models.ForeignKey(Inventorytransactiondocuments, models.DO_NOTHING, db_column='InventoryTransactionDocumentId')  # Field name made lowercase.
    inventorytransactiontypeid = models.IntegerField(db_column='InventoryTransactionTypeId')  # Field name made lowercase.
    sourcewarehouseid = models.IntegerField(db_column='SourceWarehouseId')  # Field name made lowercase.
    targetwarehouseid = models.IntegerField(db_column='TargetWarehouseId')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    unit = models.TextField(db_column='Unit', blank=True, null=True)  # Field name made lowercase.
    multiplier = models.IntegerField(db_column='Multiplier')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=16, decimal_places=3)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=16, decimal_places=2)  # Field name made lowercase.
    inventoryitem = models.ForeignKey(Inventoryitems, models.DO_NOTHING, db_column='InventoryItem_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryTransactions'


class Menuassignments(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tickettypeid = models.ForeignKey('Tickettypes', models.DO_NOTHING, db_column='TicketTypeId')  # Field name made lowercase.
    terminalid = models.IntegerField(db_column='TerminalId')  # Field name made lowercase.
    menuid = models.IntegerField(db_column='MenuId')  # Field name made lowercase.
    terminalname = models.TextField(db_column='TerminalName', blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MenuAssignments'
        unique_together = (('id', 'tickettypeid'),)


class Menuitemportions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    menuitemid = models.ForeignKey('Menuitems', models.DO_NOTHING, db_column='MenuItemId')  # Field name made lowercase.
    multiplier = models.IntegerField(db_column='Multiplier')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MenuItemPortions'


class Menuitempricedefinitions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    pricetag = models.CharField(db_column='PriceTag', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MenuItemPriceDefinitions'


class Menuitemprices(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    menuitemportionid = models.ForeignKey(Menuitemportions, models.DO_NOTHING, db_column='MenuItemPortionId')  # Field name made lowercase.
    pricetag = models.CharField(db_column='PriceTag', max_length=10, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=16, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MenuItemPrices'
        unique_together = (('id', 'menuitemportionid'),)


class Menuitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    groupcode = models.TextField(db_column='GroupCode', blank=True, null=True)  # Field name made lowercase.
    barcode = models.TextField(db_column='Barcode', blank=True, null=True)  # Field name made lowercase.
    tag = models.TextField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MenuItems'


class Numerators(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    lastupdatetime = models.TextField(db_column='LastUpdateTime')  # Field name made lowercase. This field type is a guess.
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    numberformat = models.TextField(db_column='NumberFormat', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Numerators'


class Ordertaggroups(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    columncount = models.IntegerField(db_column='ColumnCount')  # Field name made lowercase.
    buttonheight = models.IntegerField(db_column='ButtonHeight')  # Field name made lowercase.
    fontsize = models.IntegerField(db_column='FontSize')  # Field name made lowercase.
    buttoncolor = models.TextField(db_column='ButtonColor', blank=True, null=True)  # Field name made lowercase.
    maxselecteditems = models.IntegerField(db_column='MaxSelectedItems')  # Field name made lowercase.
    minselecteditems = models.IntegerField(db_column='MinSelectedItems')  # Field name made lowercase.
    addtagpricetoorderprice = models.BooleanField(db_column='AddTagPriceToOrderPrice')  # Field name made lowercase.
    freetagging = models.BooleanField(db_column='FreeTagging')  # Field name made lowercase.
    savefreetags = models.BooleanField(db_column='SaveFreeTags')  # Field name made lowercase.
    grouptag = models.TextField(db_column='GroupTag', blank=True, null=True)  # Field name made lowercase.
    taxfree = models.BooleanField(db_column='TaxFree')  # Field name made lowercase.
    hidden = models.BooleanField(db_column='Hidden')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderTagGroups'


class Ordertagmaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ordertaggroupid = models.ForeignKey(Ordertaggroups, models.DO_NOTHING, db_column='OrderTagGroupId')  # Field name made lowercase.
    menuitemgroupcode = models.TextField(db_column='MenuItemGroupCode', blank=True, null=True)  # Field name made lowercase.
    menuitemid = models.IntegerField(db_column='MenuItemId')  # Field name made lowercase.
    terminalid = models.IntegerField(db_column='TerminalId')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderTagMaps'


class Ordertags(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    ordertaggroupid = models.ForeignKey(Ordertaggroups, models.DO_NOTHING, db_column='OrderTagGroupId')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=16, decimal_places=2)  # Field name made lowercase.
    menuitemid = models.IntegerField(db_column='MenuItemId')  # Field name made lowercase.
    maxquantity = models.IntegerField(db_column='MaxQuantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderTags'


class Orders(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='TicketId')  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WarehouseId')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    menuitemid = models.IntegerField(db_column='MenuItemId')  # Field name made lowercase.
    menuitemname = models.TextField(db_column='MenuItemName', blank=True, null=True)  # Field name made lowercase.
    portionname = models.TextField(db_column='PortionName', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=16, decimal_places=2)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=16, decimal_places=3)  # Field name made lowercase.
    portioncount = models.IntegerField(db_column='PortionCount')  # Field name made lowercase.
    locked = models.BooleanField(db_column='Locked')  # Field name made lowercase.
    calculateprice = models.BooleanField(db_column='CalculatePrice')  # Field name made lowercase.
    decreaseinventory = models.BooleanField(db_column='DecreaseInventory')  # Field name made lowercase.
    increaseinventory = models.BooleanField(db_column='IncreaseInventory')  # Field name made lowercase.
    ordernumber = models.IntegerField(db_column='OrderNumber')  # Field name made lowercase.
    creatingusername = models.TextField(db_column='CreatingUserName', blank=True, null=True)  # Field name made lowercase.
    createddatetime = models.DateTimeField(db_column='CreatedDateTime')  # Field name made lowercase.
    accounttransactiontypeid = models.IntegerField(db_column='AccountTransactionTypeId')  # Field name made lowercase.
    producttimervalueid = models.ForeignKey('Producttimervalues', models.DO_NOTHING, db_column='ProductTimerValueId', blank=True, null=True)  # Field name made lowercase.
    pricetag = models.TextField(db_column='PriceTag', blank=True, null=True)  # Field name made lowercase.
    tag = models.TextField(db_column='Tag', blank=True, null=True)  # Field name made lowercase.
    taxes = models.TextField(db_column='Taxes', blank=True, null=True)  # Field name made lowercase.
    ordertags = models.TextField(db_column='OrderTags', blank=True, null=True)  # Field name made lowercase.
    orderstates = models.TextField(db_column='OrderStates', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orders'
        unique_together = (('id', 'ticketid'),)


class Paiditems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='TicketId')  # Field name made lowercase.
    key = models.TextField(db_column='Key', blank=True, null=True)  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=16, decimal_places=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaidItems'
        unique_together = (('id', 'ticketid'),)


class Paymenttypemaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    paymenttypeid = models.ForeignKey('Paymenttypes', models.DO_NOTHING, db_column='PaymentTypeId')  # Field name made lowercase.
    terminalid = models.IntegerField(db_column='TerminalId')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentTypeMaps'


class Paymenttypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    buttoncolor = models.TextField(db_column='ButtonColor', blank=True, null=True)  # Field name made lowercase.
    fontsize = models.IntegerField(db_column='FontSize')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    accounttransactiontype = models.ForeignKey(Accounttransactiontypes, models.DO_NOTHING, db_column='AccountTransactionType_Id', blank=True, null=True)  # Field name made lowercase.
    account = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='Account_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentTypes'


class Payments(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ticketid = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='TicketId')  # Field name made lowercase.
    paymenttypeid = models.IntegerField(db_column='PaymentTypeId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    accounttransactionid = models.IntegerField(db_column='AccountTransactionId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=16, decimal_places=2)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    accounttransaction = models.ForeignKey(Accounttransactions, models.DO_NOTHING, db_column='AccountTransaction_Id', blank=True, null=True,related_name='accounttransaction_payments_set')  # Field name made lowercase.
    accounttransaction_accounttransactiondocumentid = models.ForeignKey(Accounttransactions, models.DO_NOTHING, db_column='AccountTransaction_AccountTransactionDocumentId', blank=True, null=True,related_name='accounttransaction_accounttransactiondocumentid_payments_set')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payments'
        unique_together = (('id', 'ticketid'),)


class Periodicconsumptionitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    warehouseconsumptionid = models.ForeignKey('Warehouseconsumptions', models.DO_NOTHING, db_column='WarehouseConsumptionId',related_name='warehouseconsumptionid_periodicconsumptionitems_set')  # Field name made lowercase.
    periodicconsumptionid = models.ForeignKey('Warehouseconsumptions', models.DO_NOTHING, db_column='PeriodicConsumptionId',related_name='periodicconsumptionid_periodicconsumptionitems_set')  # Field name made lowercase.
    inventoryitemid = models.IntegerField(db_column='InventoryItemId')  # Field name made lowercase.
    inventoryitemname = models.TextField(db_column='InventoryItemName', blank=True, null=True)  # Field name made lowercase.
    unitname = models.TextField(db_column='UnitName', blank=True, null=True)  # Field name made lowercase.
    unitmultiplier = models.DecimalField(db_column='UnitMultiplier', max_digits=16, decimal_places=2)  # Field name made lowercase.
    instock = models.DecimalField(db_column='InStock', max_digits=16, decimal_places=3)  # Field name made lowercase.
    added = models.DecimalField(db_column='Added', max_digits=16, decimal_places=3)  # Field name made lowercase.
    removed = models.DecimalField(db_column='Removed', max_digits=16, decimal_places=3)  # Field name made lowercase.
    consumption = models.DecimalField(db_column='Consumption', max_digits=16, decimal_places=3)  # Field name made lowercase.
    physicalinventory = models.DecimalField(db_column='PhysicalInventory', max_digits=16, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=16, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeriodicConsumptionItems'
        unique_together = (('id', 'warehouseconsumptionid', 'periodicconsumptionid'),)


class Periodicconsumptions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    workperiodid = models.IntegerField(db_column='WorkPeriodId')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='LastUpdateTime')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeriodicConsumptions'


class Permissions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value')  # Field name made lowercase.
    userroleid = models.ForeignKey('Userroles', models.DO_NOTHING, db_column='UserRoleId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Permissions'


class Printjobs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    whattoprint = models.IntegerField(db_column='WhatToPrint')  # Field name made lowercase.
    useforpaidtickets = models.BooleanField(db_column='UseForPaidTickets')  # Field name made lowercase.
    excludetax = models.BooleanField(db_column='ExcludeTax')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrintJobs'


class Printermaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    printjobid = models.ForeignKey(Printjobs, models.DO_NOTHING, db_column='PrintJobId')  # Field name made lowercase.
    menuitemgroupcode = models.TextField(db_column='MenuItemGroupCode', blank=True, null=True)  # Field name made lowercase.
    menuitemid = models.IntegerField(db_column='MenuItemId')  # Field name made lowercase.
    printerid = models.IntegerField(db_column='PrinterId')  # Field name made lowercase.
    printertemplateid = models.IntegerField(db_column='PrinterTemplateId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrinterMaps'


class Printertemplates(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    template = models.TextField(db_column='Template', blank=True, null=True)  # Field name made lowercase.
    mergelines = models.BooleanField(db_column='MergeLines')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrinterTemplates'


class Printers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sharename = models.TextField(db_column='ShareName', blank=True, null=True)  # Field name made lowercase.
    printertype = models.IntegerField(db_column='PrinterType')  # Field name made lowercase.
    codepage = models.IntegerField(db_column='CodePage')  # Field name made lowercase.
    charsperline = models.IntegerField(db_column='CharsPerLine')  # Field name made lowercase.
    pageheight = models.IntegerField(db_column='PageHeight')  # Field name made lowercase.
    customprintername = models.TextField(db_column='CustomPrinterName', blank=True, null=True)  # Field name made lowercase.
    customprinterdata = models.TextField(db_column='CustomPrinterData', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Printers'


class Prodcuttimermaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    producttimerid = models.ForeignKey('Producttimers', models.DO_NOTHING, db_column='ProductTimerId')  # Field name made lowercase.
    menuitemgroupcode = models.TextField(db_column='MenuItemGroupCode', blank=True, null=True)  # Field name made lowercase.
    menuitemid = models.IntegerField(db_column='MenuItemId')  # Field name made lowercase.
    terminalid = models.IntegerField(db_column='TerminalId')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProdcutTimerMaps'


class Producttimervalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    producttimerid = models.IntegerField(db_column='ProductTimerId')  # Field name made lowercase.
    pricetype = models.IntegerField(db_column='PriceType')  # Field name made lowercase.
    priceduration = models.DecimalField(db_column='PriceDuration', max_digits=16, decimal_places=2)  # Field name made lowercase.
    mintime = models.DecimalField(db_column='MinTime', max_digits=16, decimal_places=2)  # Field name made lowercase.
    timerounding = models.DecimalField(db_column='TimeRounding', max_digits=16, decimal_places=2)  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start')  # Field name made lowercase.
    end = models.DateTimeField(db_column='End')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductTimerValues'


class Producttimers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    pricetype = models.IntegerField(db_column='PriceType')  # Field name made lowercase.
    priceduration = models.DecimalField(db_column='PriceDuration', max_digits=16, decimal_places=2)  # Field name made lowercase.
    mintime = models.DecimalField(db_column='MinTime', max_digits=16, decimal_places=2)  # Field name made lowercase.
    timerounding = models.DecimalField(db_column='TimeRounding', max_digits=16, decimal_places=2)  # Field name made lowercase.
    starttime = models.IntegerField(db_column='StartTime')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductTimers'


class Programsettingvalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=250, blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProgramSettingValues'


class Recipeitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    recipeid = models.ForeignKey('Recipes', models.DO_NOTHING, db_column='RecipeId')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=16, decimal_places=3)  # Field name made lowercase.
    inventoryitem = models.ForeignKey(Inventoryitems, models.DO_NOTHING, db_column='InventoryItem_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RecipeItems'


class Recipes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    fixedcost = models.DecimalField(db_column='FixedCost', max_digits=16, decimal_places=2)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    portion = models.ForeignKey(Menuitemportions, models.DO_NOTHING, db_column='Portion_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recipes'


class Screenmenucategories(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    screenmenuid = models.ForeignKey('Screenmenus', models.DO_NOTHING, db_column='ScreenMenuId')  # Field name made lowercase.
    mostuseditemscategory = models.BooleanField(db_column='MostUsedItemsCategory')  # Field name made lowercase.
    columncount = models.IntegerField(db_column='ColumnCount')  # Field name made lowercase.
    menuitembuttonheight = models.IntegerField(db_column='MenuItemButtonHeight')  # Field name made lowercase.
    menuitembuttoncolor = models.TextField(db_column='MenuItemButtonColor', blank=True, null=True)  # Field name made lowercase.
    menuitemfontsize = models.FloatField(db_column='MenuItemFontSize')  # Field name made lowercase.
    wraptext = models.BooleanField(db_column='WrapText')  # Field name made lowercase.
    pagecount = models.IntegerField(db_column='PageCount')  # Field name made lowercase.
    mainbuttonheight = models.IntegerField(db_column='MainButtonHeight')  # Field name made lowercase.
    mainbuttoncolor = models.TextField(db_column='MainButtonColor', blank=True, null=True)  # Field name made lowercase.
    mainfontsize = models.FloatField(db_column='MainFontSize')  # Field name made lowercase.
    subbuttonheight = models.IntegerField(db_column='SubButtonHeight')  # Field name made lowercase.
    subbuttonrows = models.IntegerField(db_column='SubButtonRows')  # Field name made lowercase.
    subbuttoncolordef = models.TextField(db_column='SubButtonColorDef', blank=True, null=True)  # Field name made lowercase.
    numeratortype = models.IntegerField(db_column='NumeratorType')  # Field name made lowercase.
    numeratorvalues = models.TextField(db_column='NumeratorValues', blank=True, null=True)  # Field name made lowercase.
    alphabuttonvalues = models.TextField(db_column='AlphaButtonValues', blank=True, null=True)  # Field name made lowercase.
    imagepath = models.TextField(db_column='ImagePath', blank=True, null=True)  # Field name made lowercase.
    maxitems = models.IntegerField(db_column='MaxItems')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScreenMenuCategories'


class Screenmenuitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    screenmenucategoryid = models.ForeignKey(Screenmenucategories, models.DO_NOTHING, db_column='ScreenMenuCategoryId')  # Field name made lowercase.
    menuitemid = models.IntegerField(db_column='MenuItemId')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    autoselect = models.BooleanField(db_column='AutoSelect')  # Field name made lowercase.
    buttoncolor = models.TextField(db_column='ButtonColor', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    imagepath = models.TextField(db_column='ImagePath', blank=True, null=True)  # Field name made lowercase.
    fontsize = models.FloatField(db_column='FontSize')  # Field name made lowercase.
    submenutag = models.TextField(db_column='SubMenuTag', blank=True, null=True)  # Field name made lowercase.
    itemportion = models.TextField(db_column='ItemPortion', blank=True, null=True)  # Field name made lowercase.
    ordertags = models.TextField(db_column='OrderTags', blank=True, null=True)  # Field name made lowercase.
    orderstates = models.TextField(db_column='OrderStates', blank=True, null=True)  # Field name made lowercase.
    automationcommand = models.TextField(db_column='AutomationCommand', blank=True, null=True)  # Field name made lowercase.
    automationcommandvalue = models.TextField(db_column='AutomationCommandValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScreenMenuItems'


class Screenmenus(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    categorycolumncount = models.IntegerField(db_column='CategoryColumnCount')  # Field name made lowercase.
    categorycolumnwidthrate = models.IntegerField(db_column='CategoryColumnWidthRate')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScreenMenus'


class Scripts(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    handlername = models.TextField(db_column='HandlerName', blank=True, null=True)  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Scripts'


class States(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    groupname = models.TextField(db_column='GroupName', blank=True, null=True)  # Field name made lowercase.
    statetype = models.IntegerField(db_column='StateType')  # Field name made lowercase.
    color = models.TextField(db_column='Color', blank=True, null=True)  # Field name made lowercase.
    showonendofdayreport = models.BooleanField(db_column='ShowOnEndOfDayReport')  # Field name made lowercase.
    showonproductreport = models.BooleanField(db_column='ShowOnProductReport')  # Field name made lowercase.
    showonticket = models.BooleanField(db_column='ShowOnTicket')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'States'


class Taskcustomfields(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tasktypeid = models.ForeignKey('Tasktypes', models.DO_NOTHING, db_column='TaskTypeId')  # Field name made lowercase.
    fieldtype = models.IntegerField(db_column='FieldType')  # Field name made lowercase.
    editingformat = models.TextField(db_column='EditingFormat', blank=True, null=True)  # Field name made lowercase.
    displayformat = models.TextField(db_column='DisplayFormat', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskCustomFields'
        unique_together = (('id', 'tasktypeid'),)


class Tasktokens(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    taskid = models.ForeignKey('Tasks', models.DO_NOTHING, db_column='TaskId')  # Field name made lowercase.
    caption = models.TextField(db_column='Caption', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    referencetypeid = models.IntegerField(db_column='ReferenceTypeId')  # Field name made lowercase.
    referenceid = models.IntegerField(db_column='ReferenceId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskTokens'
        unique_together = (('id', 'taskid'),)


class Tasktypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaskTypes'


class Tasks(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tasktypeid = models.IntegerField(db_column='TaskTypeId')  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    customdata = models.TextField(db_column='CustomData', blank=True, null=True)  # Field name made lowercase.
    completed = models.BooleanField(db_column='Completed')  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='LastUpdateTime')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tasks'


class Taxtemplatemaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    taxtemplateid = models.ForeignKey('Taxtemplates', models.DO_NOTHING, db_column='TaxTemplateId')  # Field name made lowercase.
    menuitemgroupcode = models.TextField(db_column='MenuItemGroupCode', blank=True, null=True)  # Field name made lowercase.
    menuitemid = models.IntegerField(db_column='MenuItemId')  # Field name made lowercase.
    terminalid = models.IntegerField(db_column='TerminalId')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaxTemplateMaps'


class Taxtemplates(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=16, decimal_places=2)  # Field name made lowercase.
    rounding = models.IntegerField(db_column='Rounding')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    accounttransactiontype = models.ForeignKey(Accounttransactiontypes, models.DO_NOTHING, db_column='AccountTransactionType_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaxTemplates'


class Terminals(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault')  # Field name made lowercase.
    autologout = models.BooleanField(db_column='AutoLogout')  # Field name made lowercase.
    reportprinterid = models.IntegerField(db_column='ReportPrinterId')  # Field name made lowercase.
    transactionprinterid = models.IntegerField(db_column='TransactionPrinterId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Terminals'


class Ticketentities(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    entitytypeid = models.IntegerField(db_column='EntityTypeId')  # Field name made lowercase.
    entityid = models.IntegerField(db_column='EntityId')  # Field name made lowercase.
    accountid = models.IntegerField(db_column='AccountId')  # Field name made lowercase.
    accounttypeid = models.IntegerField(db_column='AccountTypeId')  # Field name made lowercase.
    entityname = models.TextField(db_column='EntityName', blank=True, null=True)  # Field name made lowercase.
    entitycustomdata = models.TextField(db_column='EntityCustomData', blank=True, null=True)  # Field name made lowercase.
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='Ticket_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketEntities'


class Tickettaggroups(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    freetagging = models.BooleanField(db_column='FreeTagging')  # Field name made lowercase.
    savefreetags = models.BooleanField(db_column='SaveFreeTags')  # Field name made lowercase.
    buttoncolorwhentagselected = models.TextField(db_column='ButtonColorWhenTagSelected', blank=True, null=True)  # Field name made lowercase.
    buttoncolorwhennotagselected = models.TextField(db_column='ButtonColorWhenNoTagSelected', blank=True, null=True)  # Field name made lowercase.
    forcevalue = models.BooleanField(db_column='ForceValue')  # Field name made lowercase.
    askbeforecreatingticket = models.BooleanField(db_column='AskBeforeCreatingTicket')  # Field name made lowercase.
    datatype = models.IntegerField(db_column='DataType')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketTagGroups'


class Tickettagmaps(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tickettaggroupid = models.ForeignKey(Tickettaggroups, models.DO_NOTHING, db_column='TicketTagGroupId')  # Field name made lowercase.
    terminalid = models.IntegerField(db_column='TerminalId')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    userroleid = models.IntegerField(db_column='UserRoleId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketTagMaps'


class Tickettags(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tickettaggroupid = models.ForeignKey(Tickettaggroups, models.DO_NOTHING, db_column='TicketTagGroupId')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketTags'


class Tickettypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    screenmenuid = models.IntegerField(db_column='ScreenMenuId')  # Field name made lowercase.
    taxincluded = models.BooleanField(db_column='TaxIncluded')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    ticketnumerator = models.ForeignKey(Numerators, models.DO_NOTHING, db_column='TicketNumerator_Id', blank=True, null=True,related_name='ticketnumerator_tickettypes_set')  # Field name made lowercase.
    ordernumerator = models.ForeignKey(Numerators, models.DO_NOTHING, db_column='OrderNumerator_Id', blank=True, null=True,related_name='ordernumerator_tickettypes_set')  # Field name made lowercase.
    saletransactiontype = models.ForeignKey(Accounttransactiontypes, models.DO_NOTHING, db_column='SaleTransactionType_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TicketTypes'


class Tickets(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='LastUpdateTime')  # Field name made lowercase.
    ticketnumber = models.TextField(db_column='TicketNumber', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    lastorderdate = models.DateTimeField(db_column='LastOrderDate')  # Field name made lowercase.
    lastpaymentdate = models.DateTimeField(db_column='LastPaymentDate')  # Field name made lowercase.
    isclosed = models.BooleanField(db_column='IsClosed')  # Field name made lowercase.
    islocked = models.BooleanField(db_column='IsLocked')  # Field name made lowercase.
    remainingamount = models.DecimalField(db_column='RemainingAmount', max_digits=16, decimal_places=2)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=16, decimal_places=2)  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    tickettypeid = models.IntegerField(db_column='TicketTypeId')  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedusername = models.TextField(db_column='LastModifiedUserName', blank=True, null=True)  # Field name made lowercase.
    tickettags = models.TextField(db_column='TicketTags', blank=True, null=True)  # Field name made lowercase.
    ticketstates = models.TextField(db_column='TicketStates', blank=True, null=True)  # Field name made lowercase.
    ticketlogs = models.TextField(db_column='TicketLogs', blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='ExchangeRate', max_digits=18, decimal_places=2)  # Field name made lowercase.
    taxincluded = models.BooleanField(db_column='TaxIncluded')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    transactiondocument = models.ForeignKey(Accounttransactiondocuments, models.DO_NOTHING, db_column='TransactionDocument_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tickets'


class Triggers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    expression = models.TextField(db_column='Expression', blank=True, null=True)  # Field name made lowercase.
    lasttrigger = models.DateTimeField(db_column='LastTrigger')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Triggers'


class Userroles(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    isadmin = models.BooleanField(db_column='IsAdmin')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserRoles'


class Users(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    pincode = models.TextField(db_column='PinCode', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    userrole = models.ForeignKey(Userroles, models.DO_NOTHING, db_column='UserRole_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class Versioninfo(models.Model):
    version = models.BigIntegerField(db_column='Version')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VersionInfo'


class Warehouseconsumptions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    periodicconsumptionid = models.ForeignKey(Periodicconsumptions, models.DO_NOTHING, db_column='PeriodicConsumptionId')  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WarehouseId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WarehouseConsumptions'
        unique_together = (('id', 'periodicconsumptionid'),)


class Warehousetypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WarehouseTypes'


class Warehouses(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    warehousetypeid = models.IntegerField(db_column='WarehouseTypeId')  # Field name made lowercase.
    sortorder = models.IntegerField(db_column='SortOrder')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Warehouses'


class Widgets(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    entityscreenid = models.ForeignKey(Entityscreens, models.DO_NOTHING, db_column='EntityScreenId')  # Field name made lowercase.
    xlocation = models.IntegerField(db_column='XLocation')  # Field name made lowercase.
    ylocation = models.IntegerField(db_column='YLocation')  # Field name made lowercase.
    height = models.IntegerField(db_column='Height')  # Field name made lowercase.
    width = models.IntegerField(db_column='Width')  # Field name made lowercase.
    cornerradius = models.IntegerField(db_column='CornerRadius')  # Field name made lowercase.
    angle = models.FloatField(db_column='Angle')  # Field name made lowercase.
    scale = models.FloatField(db_column='Scale')  # Field name made lowercase.
    properties = models.TextField(db_column='Properties', blank=True, null=True)  # Field name made lowercase.
    creatorname = models.TextField(db_column='CreatorName', blank=True, null=True)  # Field name made lowercase.
    autorefresh = models.BooleanField(db_column='AutoRefresh')  # Field name made lowercase.
    autorefreshinterval = models.IntegerField(db_column='AutoRefreshInterval')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Widgets'


class Workperiods(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    startdescription = models.TextField(db_column='StartDescription', blank=True, null=True)  # Field name made lowercase.
    enddescription = models.TextField(db_column='EndDescription', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkPeriods'


class Migrationhistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=255)  # Field name made lowercase.
    model = models.BinaryField(db_column='Model')  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__MigrationHistory'
