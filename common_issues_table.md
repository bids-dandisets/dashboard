# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator




## `nwb2bids` Notifications

|            Severity            |                                                                                Title                                                                                 |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :----------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|    STYLE_SUGGESTION (ERROR)    |                [Invalid session ID](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L1431)                 |          37499           |              26483              |
|    STYLE_SUGGESTION (ERROR)    |               [Invalid participant ID](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/nwb2bids_notifications.json#L43)                |          29032           |              18470              |
|  SCHEMA_INVALIDATION (ERROR)   |                  [Invalid species](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L1417)                  |           2831           |              2831               |
| SCHEMA_INVALIDATION (CRITICAL) |               [Missing participant sex](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)                |           1170           |              1170               |
|    STYLE_SUGGESTION (INFO)     |                [Missing description](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3384)                |           754            |               754               |
|    STYLE_SUGGESTION (ERROR)    |          [Invalid participant sex (BIDS)](https://github.com/bids-dandisets///000016/blob/draft/derivatives/validations/nwb2bids_notifications.json#L4470)           |           496            |               496               |
|    STYLE_SUGGESTION (ERROR)    |        [Invalid participant sex (archives)](https://github.com/bids-dandisets///000016/blob/draft/derivatives/validations/nwb2bids_notifications.json#L7035)         |           346            |               346               |
|     INTERNAL_ERROR (ERROR)     |  [Failed to initialize converter on remote Dandiset](https://github.com/bids-dandisets///000034/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)   |           261            |               261               |
|     INTERNAL_ERROR (INFO)      |           [INFO: invalid Dandiset metadata](https://github.com/bids-dandisets///000005/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)            |           140            |               140               |
|     INTERNAL_ERROR (ERROR)     | [Failed to extract metadata for one or more sessions](https://github.com/bids-dandisets///000020/blob/draft/derivatives/validations/nwb2bids_notifications.json#L15) |           102            |               104               |
|     INTERNAL_ERROR (ERROR)     |          [Failed to convert to BIDS dataset](https://github.com/bids-dandisets///000020/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)           |           102            |               102               |
|     INTERNAL_ERROR (ERROR)     |               [Dandiset is already BIDS](https://github.com/bids-dandisets///000026/blob/draft/derivatives/validations/nwb2bids_notifications.json#L3)               |            24            |               24                |
| SCHEMA_INVALIDATION (WARNING)  |      [WARNING: multiple licenses not supported](https://github.com/bids-dandisets///000156/blob/draft/derivatives/validations/nwb2bids_notifications.json#L15)       |            4             |                4                |
| SCHEMA_INVALIDATION (CRITICAL) |             [Missing participant species](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/nwb2bids_notifications.json#L15)             |            4             |                4                |