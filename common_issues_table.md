# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |                                                                  Title                                                                   |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :--------: | :--------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
|  WARNING   |       [JSON_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L1)       |           955            |                6                |
|  WARNING   |         [SUBJECT_FOLDERS](https://github.com/bids-dandisets///000004/blob/draft/derivatives/validations/bids_validation.txt#L1)          |           631            |                2                |
|  WARNING   |           [NO_AUTHORS](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L31)            |           100            |                2                |
|   ERROR    |        [JSON_KEY_REQUIRED](https://github.com/bids-dandisets///000021/blob/draft/derivatives/validations/bids_validation.txt#L41)        |           100            |                2                |
|  WARNING   |     [SIDECAR_KEY_RECOMMENDED](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L13)     |           2317           |                0                |
|  WARNING   | [SUSPICIOUS_POSITIVE_EVENT_ONSET](https://github.com/bids-dandisets///000061/blob/draft/derivatives/validations/bids_validation.txt#L13) |            39            |                0                |
|  WARNING   |    [TSV_COLUMN_TYPE_REDEFINED](https://github.com/bids-dandisets///000402/blob/draft/derivatives/validations/bids_validation.txt#L26)    |           327            |                0                |
|  WARNING   |        [EVENT_ONSET_ORDER](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L35)        |           305            |                0                |
|   ERROR    |    [TSV_VALUE_INCORRECT_TYPE](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L26)     |           1301           |                0                |
|   ERROR    |      [INVALID_ENTITY_LABEL](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L39)       |          16395           |                0                |
|   ERROR    |            [HED_ERROR](https://github.com/bids-dandisets///000003/blob/draft/derivatives/validations/bids_validation.txt#L47)            |           456            |                0                |
|   ERROR    |          [NOT_INCLUDED](https://github.com/bids-dandisets///000008/blob/draft/derivatives/validations/bids_validation.txt#L19)           |          36025           |                0                |
|   ERROR    |  [JSON_SCHEMA_VALIDATION_ERROR](https://github.com/bids-dandisets///000018/blob/draft/derivatives/validations/bids_validation.txt#L19)   |           1376           |                0                |
|   ERROR    |    [SIDECAR_WITHOUT_DATAFILE](https://github.com/bids-dandisets///000043/blob/draft/derivatives/validations/bids_validation.txt#L33)     |           162            |                0                |
|   ERROR    |         [TSV_EQUAL_ROWS](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L64)          |           305            |                0                |
|   ERROR    |       [TSV_COLUMN_MISSING](https://github.com/bids-dandisets///001169/blob/draft/derivatives/validations/bids_validation.txt#L80)        |           610            |                0                |


## `nwb2bids` Notifications

|         Severity         |                                                                                    Title                                                                                    |  Count<br>(Unsanitized)  |  Count<br>(Basic sanitization)  |
| :----------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :-----------------------------: |
| STYLE_SUGGESTION (ERROR) |                [Invalid session ID](https://github.com/bids-dandisets///000341/basic_sanitization/derivatives/validations/nwb2bids_notifications.json#L129)                 |            0             |               326               |
| STYLE_SUGGESTION (ERROR) |           [Invalid participant sex (BIDS)](https://github.com/bids-dandisets///000341/basic_sanitization/derivatives/validations/nwb2bids_notifications.json#L15)           |            0             |                6                |
|  INTERNAL_ERROR (ERROR)  | [Failed to extract metadata for one or more sessions](https://github.com/bids-dandisets///000341/basic_sanitization/derivatives/validations/nwb2bids_notifications.json#L3) |            0             |                1                |