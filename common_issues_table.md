# Common Issues in BIDS Dandisets

This table summarizes common issues found in BIDS dandisets processed with nwb2bids.



## BIDS Validator

|  Severity  |             Message              |  Count (Unsanitized)  |  Count (Basic sanitization)  |
| :--------: | :------------------------------: | :-------------------: | :--------------------------: |
|   ERROR    |     TSV_VALUE_INCORRECT_TYPE     |           7           |              7               |
|   ERROR    |    TSV_INDEX_VALUE_NOT_UNIQUE    |           5           |              5               |
|   ERROR    |     PARTICIPANT_ID_MISMATCH      |           4           |              4               |
|   ERROR    |       REQUIRED_COORDSYSTEM       |           4           |              4               |
|   ERROR    |       INVALID_ENTITY_LABEL       |           4           |              0               |
|  WARNING   |       JSON_KEY_RECOMMENDED       |           6           |              6               |
|  WARNING   |     SIDECAR_KEY_RECOMMENDED      |           6           |              6               |
|  WARNING   | TSV_ADDITIONAL_COLUMNS_UNDEFINED |           5           |              5               |
|  WARNING   |         SUBJECT_FOLDERS          |           4           |              4               |


## `nwb2bids` Notifications

|            Severity            |             Message             |  Count (Unsanitized)  |  Count (Basic sanitization)  |
| :----------------------------: | :-----------------------------: | :-------------------: | :--------------------------: |
|    STYLE_SUGGESTION (ERROR)    |       Invalid session ID        |          10           |              10              |
| SCHEMA_INVALIDATION (CRITICAL) |     Missing participant sex     |          10           |              10              |
|     INTERNAL_ERROR (INFO)      | INFO: invalid Dandiset metadata |          10           |              10              |
|  SCHEMA_INVALIDATION (ERROR)   |         Invalid species         |          10           |              10              |
