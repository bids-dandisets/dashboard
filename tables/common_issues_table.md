# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |              Title              |                                             Count<br>(Unsanitized)                                             |                                                Count<br>(Basic sanitization)                                                 |
| :--------: | :-----------------------------: | :------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------: |
|  WARNING   |     SIDECAR_KEY_RECOMMENDED     | [79462](https://github.com/bids-dandisets//000003/blob/draft/derivatives/validations/bids_validation.txt#L13)  | [323440](https://github.com/bids-dandisets//000003/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L46)  |
|   ERROR    |      SIDECAR_KEY_REQUIRED       | [13083](https://github.com/bids-dandisets//000402/blob/draft/derivatives/validations/bids_validation.txt#L119) | [105627](https://github.com/bids-dandisets//000016/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L105) |
|  WARNING   |    TSV_COLUMN_TYPE_REDEFINED    | [39808](https://github.com/bids-dandisets//000003/blob/draft/derivatives/validations/bids_validation.txt#L70)  |  [65902](https://github.com/bids-dandisets//000003/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L13)  |
|   ERROR    |   TSV_INDEX_VALUE_NOT_UNIQUE    | [3584](https://github.com/bids-dandisets//000638/blob/draft/derivatives/validations/bids_validation.txt#L124)  | [13334](https://github.com/bids-dandisets//000638/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L116)  |
|   ERROR    |       TSV_COLUMN_MISSING        |  [826](https://github.com/bids-dandisets//001169/blob/draft/derivatives/validations/bids_validation.txt#L193)  |  [938](https://github.com/bids-dandisets//000568/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L111)   |
|  WARNING   |      JSON_KEY_RECOMMENDED       |   [741](https://github.com/bids-dandisets//000003/blob/draft/derivatives/validations/bids_validation.txt#L1)   |   [745](https://github.com/bids-dandisets//000003/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L1)    |
|  WARNING   |        EVENT_ONSET_ORDER        |  [413](https://github.com/bids-dandisets//001169/blob/draft/derivatives/validations/bids_validation.txt#L118)  |   [549](https://github.com/bids-dandisets//000016/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L96)   |
|   ERROR    |         TSV_EQUAL_ROWS          |  [413](https://github.com/bids-dandisets//001169/blob/draft/derivatives/validations/bids_validation.txt#L185)  |  [469](https://github.com/bids-dandisets//000568/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L103)   |
|  WARNING   |         SUBJECT_FOLDERS         |   [381](https://github.com/bids-dandisets//000004/blob/draft/derivatives/validations/bids_validation.txt#L1)   |   [382](https://github.com/bids-dandisets//000004/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L1)    |
|   ERROR    |  JSON_SCHEMA_VALIDATION_ERROR   |  [354](https://github.com/bids-dandisets//000028/blob/draft/derivatives/validations/bids_validation.txt#L19)   |   [358](https://github.com/bids-dandisets//000028/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L19)   |
|   ERROR    |    TSV_VALUE_INCORRECT_TYPE     |  [705](https://github.com/bids-dandisets//000003/blob/draft/derivatives/validations/bids_validation.txt#L103)  |  [285](https://github.com/bids-dandisets//000003/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L103)   |
|  WARNING   |           NO_AUTHORS            |  [127](https://github.com/bids-dandisets//000021/blob/draft/derivatives/validations/bids_validation.txt#L31)   |   [128](https://github.com/bids-dandisets//000021/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L31)   |
|   ERROR    |        JSON_KEY_REQUIRED        |  [127](https://github.com/bids-dandisets//000021/blob/draft/derivatives/validations/bids_validation.txt#L41)   |   [128](https://github.com/bids-dandisets//000021/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L41)   |
|  WARNING   | SUSPICIOUS_POSITIVE_EVENT_ONSET |  [39](https://github.com/bids-dandisets//000061/blob/draft/derivatives/validations/bids_validation.txt#L103)   |   [41](https://github.com/bids-dandisets//000061/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L103)   |
|  WARNING   | SUSPICIOUS_NEGATIVE_EVENT_ONSET |                                                       0                                                        |    [2](https://github.com/bids-dandisets//001371/blob/basic_sanitization/derivatives/validations/bids_validation.txt#L88)    |
|   ERROR    |      INVALID_ENTITY_LABEL       | [19522](https://github.com/bids-dandisets//000003/blob/draft/derivatives/validations/bids_validation.txt#L116) |                                                              0                                                               |
|   ERROR    |          NOT_INCLUDED           | [34964](https://github.com/bids-dandisets//000008/blob/draft/derivatives/validations/bids_validation.txt#L19)  |                                                              0                                                               |
|   ERROR    |    SIDECAR_WITHOUT_DATAFILE     |  [341](https://github.com/bids-dandisets//000043/blob/draft/derivatives/validations/bids_validation.txt#L33)   |                                                              0                                                               |


## `nwb2bids` Notifications

