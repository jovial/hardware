# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


def read_smart_scsi_result():
    return [('disk', 'fake', 'SMART/vendor', 'SEAGATE'),
            ('disk', 'fake', 'SMART/product', 'ST9300605SS'),
            ('disk', 'fake', 'SMART/serial_number', '6XP2FK730000M233QACC'),
            ('disk', 'fake', 'SMART/health', 'OK'),
            ('disk', 'fake', 'SMART/current_drive_temperature', '36'),
            ('disk', 'fake', 'SMART/current_drive_temperature_unit', 'C'),
            ('disk', 'fake', 'SMART/drive_trip_temperature', '68'),
            ('disk', 'fake', 'SMART/drive_trip_temperature_unit', 'C'),
            ('disk', 'fake', 'SMART/manufacture_date', 'week 10 of year 2012'),
            ('disk', 'fake',
             'SMART/specified_start_stop_cycle_count_over_lifetime', '10000'),
            ('disk', 'fake', 'SMART/start_stop_cycle_count', '8'),
            ('disk', 'fake', 'SMART/specified_load_count_over_lifetime',
             '300000'),
            ('disk', 'fake', 'SMART/load_count', '8'),
            ('disk', 'fake', 'SMART/blocks_sent', '3424156415'),
            ('disk', 'fake', 'SMART/blocks_received', '2906714357'),
            ('disk', 'fake', 'SMART/blocks_read_from_cache', '120574148'),
            ('disk', 'fake', 'SMART/power_on_hours', '14491.72'),
            ('disk', 'fake', 'SMART/read_total_corrected_errors',
             '1521076288'),
            ('disk', 'fake', 'SMART/read_gigabytes_processed', '25920.949'),
            ('disk', 'fake', 'SMART/read_total_uncorrected_errors', '0'),
            ('disk', 'fake', 'SMART/write_total_corrected_errors', '0'),
            ('disk', 'fake', 'SMART/write_gigabytes_processed', '1543.290'),
            ('disk', 'fake', 'SMART/write_total_uncorrected_errors', '0'),
            ('disk', 'fake', 'SMART/non_medium_errors_count', '6')]


def read_smart_ata_result():
    return [('disk', 'fake', 'SMART/device_model', 'ST3000DM001-9YN166'),
            ('disk', 'fake', 'SMART/serial_number', 'W1F09S26'),
            ('disk', 'fake', 'SMART/firmware_version', 'CC4C'),
            ('disk', 'fake', 'SMART/Raw_Read_Error_Rate(1)/value', '111'),
            ('disk', 'fake', 'SMART/Raw_Read_Error_Rate(1)/worst', '099'),
            ('disk', 'fake', 'SMART/Raw_Read_Error_Rate(1)/thresh', '006'),
            ('disk', 'fake', 'SMART/Raw_Read_Error_Rate(1)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Raw_Read_Error_Rate(1)/raw', ' 34053632'),
            ('disk', 'fake', 'SMART/Spin_Up_Time(3)/value', '093'),
            ('disk', 'fake', 'SMART/Spin_Up_Time(3)/worst', '092'),
            ('disk', 'fake', 'SMART/Spin_Up_Time(3)/thresh', '000'),
            ('disk', 'fake', 'SMART/Spin_Up_Time(3)/when_failed', 'NEVER'),
            ('disk', 'fake', 'SMART/Spin_Up_Time(3)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Start_Stop_Count(4)/value', '100'),
            ('disk', 'fake', 'SMART/Start_Stop_Count(4)/worst', '100'),
            ('disk', 'fake', 'SMART/Start_Stop_Count(4)/thresh', '020'),
            ('disk', 'fake', 'SMART/Start_Stop_Count(4)/when_failed', 'NEVER'),
            ('disk', 'fake', 'SMART/Start_Stop_Count(4)/raw', ' 32'),
            ('disk', 'fake', 'SMART/Reallocated_Sector_Ct(5)/value', '100'),
            ('disk', 'fake', 'SMART/Reallocated_Sector_Ct(5)/worst', '100'),
            ('disk', 'fake', 'SMART/Reallocated_Sector_Ct(5)/thresh', '036'),
            ('disk', 'fake', 'SMART/Reallocated_Sector_Ct(5)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Reallocated_Sector_Ct(5)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Seek_Error_Rate(7)/value', '060'),
            ('disk', 'fake', 'SMART/Seek_Error_Rate(7)/worst', '055'),
            ('disk', 'fake', 'SMART/Seek_Error_Rate(7)/thresh', '030'),
            ('disk', 'fake', 'SMART/Seek_Error_Rate(7)/when_failed', 'NEVER'),
            ('disk', 'fake', 'SMART/Seek_Error_Rate(7)/raw', ' 21480133713'),
            ('disk', 'fake', 'SMART/Power_On_Hours(9)/value', '097'),
            ('disk', 'fake', 'SMART/Power_On_Hours(9)/worst', '097'),
            ('disk', 'fake', 'SMART/Power_On_Hours(9)/thresh', '000'),
            ('disk', 'fake', 'SMART/Power_On_Hours(9)/when_failed', 'NEVER'),
            ('disk', 'fake', 'SMART/Power_On_Hours(9)/raw', ' 2696'),
            ('disk', 'fake', 'SMART/Spin_Retry_Count(10)/value', '100'),
            ('disk', 'fake', 'SMART/Spin_Retry_Count(10)/worst', '100'),
            ('disk', 'fake', 'SMART/Spin_Retry_Count(10)/thresh', '097'),
            ('disk', 'fake', 'SMART/Spin_Retry_Count(10)/when_failed', 'NEVER'),
            ('disk', 'fake', 'SMART/Spin_Retry_Count(10)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Power_Cycle_Count(12)/value', '100'),
            ('disk', 'fake', 'SMART/Power_Cycle_Count(12)/worst', '100'),
            ('disk', 'fake', 'SMART/Power_Cycle_Count(12)/thresh', '020'),
            ('disk', 'fake', 'SMART/Power_Cycle_Count(12)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Power_Cycle_Count(12)/raw', ' 32'),
            ('disk', 'fake', 'SMART/Runtime_Bad_Block(183)/value', '100'),
            ('disk', 'fake', 'SMART/Runtime_Bad_Block(183)/worst', '100'),
            ('disk', 'fake', 'SMART/Runtime_Bad_Block(183)/thresh', '000'),
            ('disk', 'fake', 'SMART/Runtime_Bad_Block(183)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Runtime_Bad_Block(183)/raw', ' 0'),
            ('disk', 'fake', 'SMART/End-to-End_Error(184)/value', '100'),
            ('disk', 'fake', 'SMART/End-to-End_Error(184)/worst', '100'),
            ('disk', 'fake', 'SMART/End-to-End_Error(184)/thresh', '099'),
            ('disk', 'fake', 'SMART/End-to-End_Error(184)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/End-to-End_Error(184)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Reported_Uncorrect(187)/value', '100'),
            ('disk', 'fake', 'SMART/Reported_Uncorrect(187)/worst', '100'),
            ('disk', 'fake', 'SMART/Reported_Uncorrect(187)/thresh', '000'),
            ('disk', 'fake', 'SMART/Reported_Uncorrect(187)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Reported_Uncorrect(187)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Command_Timeout(188)/value', '100'),
            ('disk', 'fake', 'SMART/Command_Timeout(188)/worst', '100'),
            ('disk', 'fake', 'SMART/Command_Timeout(188)/thresh', '000'),
            ('disk', 'fake', 'SMART/Command_Timeout(188)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Command_Timeout(188)/raw', ' 0'),
            ('disk', 'fake', 'SMART/High_Fly_Writes(189)/value', '100'),
            ('disk', 'fake', 'SMART/High_Fly_Writes(189)/worst', '100'),
            ('disk', 'fake', 'SMART/High_Fly_Writes(189)/thresh', '000'),
            ('disk', 'fake', 'SMART/High_Fly_Writes(189)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/High_Fly_Writes(189)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Airflow_Temperature_Cel(190)/value', '064'),
            ('disk', 'fake', 'SMART/Airflow_Temperature_Cel(190)/worst', '061'),
            ('disk', 'fake', 'SMART/Airflow_Temperature_Cel(190)/thresh',
             '045'),
            ('disk', 'fake', 'SMART/Airflow_Temperature_Cel(190)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Airflow_Temperature_Cel(190)/raw',
             ' 36 (Min/Max 34/38)'),
            ('disk', 'fake', 'SMART/G-Sense_Error_Rate(191)/value', '100'),
            ('disk', 'fake', 'SMART/G-Sense_Error_Rate(191)/worst', '100'),
            ('disk', 'fake', 'SMART/G-Sense_Error_Rate(191)/thresh', '000'),
            ('disk', 'fake', 'SMART/G-Sense_Error_Rate(191)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/G-Sense_Error_Rate(191)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Power-Off_Retract_Count(192)/value',
             '100'),
            ('disk', 'fake', 'SMART/Power-Off_Retract_Count(192)/worst',
             '100'),
            ('disk', 'fake', 'SMART/Power-Off_Retract_Count(192)/thresh',
             '000'),
            ('disk', 'fake', 'SMART/Power-Off_Retract_Count(192)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Power-Off_Retract_Count(192)/raw', ' 28'),
            ('disk', 'fake', 'SMART/Load_Cycle_Count(193)/value', '100'),
            ('disk', 'fake', 'SMART/Load_Cycle_Count(193)/worst', '100'),
            ('disk', 'fake', 'SMART/Load_Cycle_Count(193)/thresh', '000'),
            ('disk', 'fake', 'SMART/Load_Cycle_Count(193)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Load_Cycle_Count(193)/raw', ' 63'),
            ('disk', 'fake', 'SMART/Temperature_Celsius(194)/value', '036'),
            ('disk', 'fake', 'SMART/Temperature_Celsius(194)/worst', '040'),
            ('disk', 'fake', 'SMART/Temperature_Celsius(194)/thresh', '000'),
            ('disk', 'fake', 'SMART/Temperature_Celsius(194)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Temperature_Celsius(194)/raw',
             ' 36 (0 19 0 0)'),
            ('disk', 'fake', 'SMART/Current_Pending_Sector(197)/value', '100'),
            ('disk', 'fake', 'SMART/Current_Pending_Sector(197)/worst', '100'),
            ('disk', 'fake', 'SMART/Current_Pending_Sector(197)/thresh',
             '000'),
            ('disk', 'fake',
             'SMART/Current_Pending_Sector(197)/when_failed', 'NEVER'),
            ('disk', 'fake', 'SMART/Current_Pending_Sector(197)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Offline_Uncorrectable(198)/value', '100'),
            ('disk', 'fake', 'SMART/Offline_Uncorrectable(198)/worst', '100'),
            ('disk', 'fake', 'SMART/Offline_Uncorrectable(198)/thresh', '000'),
            ('disk', 'fake', 'SMART/Offline_Uncorrectable(198)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Offline_Uncorrectable(198)/raw', ' 0'),
            ('disk', 'fake', 'SMART/UDMA_CRC_Error_Count(199)/value', '200'),
            ('disk', 'fake', 'SMART/UDMA_CRC_Error_Count(199)/worst', '200'),
            ('disk', 'fake', 'SMART/UDMA_CRC_Error_Count(199)/thresh', '000'),
            ('disk', 'fake', 'SMART/UDMA_CRC_Error_Count(199)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/UDMA_CRC_Error_Count(199)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Head_Flying_Hours(240)/value', '100'),
            ('disk', 'fake', 'SMART/Head_Flying_Hours(240)/worst', '253'),
            ('disk', 'fake', 'SMART/Head_Flying_Hours(240)/thresh', '000'),
            ('disk', 'fake', 'SMART/Head_Flying_Hours(240)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Head_Flying_Hours(240)/raw',
             ' 43748536879750'),
            ('disk', 'fake', 'SMART/Total_LBAs_Written(241)/value', '100'),
            ('disk', 'fake', 'SMART/Total_LBAs_Written(241)/worst', '253'),
            ('disk', 'fake', 'SMART/Total_LBAs_Written(241)/thresh', '000'),
            ('disk', 'fake', 'SMART/Total_LBAs_Written(241)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Total_LBAs_Written(241)/raw',
             ' 2867098636991'),
            ('disk', 'fake', 'SMART/Total_LBAs_Read(242)/value', '100'),
            ('disk', 'fake', 'SMART/Total_LBAs_Read(242)/worst', '253'),
            ('disk', 'fake', 'SMART/Total_LBAs_Read(242)/thresh', '000'),
            ('disk', 'fake', 'SMART/Total_LBAs_Read(242)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Total_LBAs_Read(242)/raw',
             ' 17478042509157')]


def read_smart_ata_decode_ignore_result():
    return [('disk', 'fake', 'SMART/device_model', 'FUJITSU MHZ2250BK G2'),
            ('disk', 'fake', 'SMART/serial_number', 'K85ET9625FV4'),
            ('disk', 'fake', 'SMART/firmware_version', '8A22'),
            ('disk', 'fake', 'SMART/Raw_Read_Error_Rate(1)/value', '100'),
            ('disk', 'fake', 'SMART/Raw_Read_Error_Rate(1)/worst', '100'),
            ('disk', 'fake', 'SMART/Raw_Read_Error_Rate(1)/thresh', '046'),
            ('disk', 'fake', 'SMART/Raw_Read_Error_Rate(1)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Raw_Read_Error_Rate(1)/raw', ' 119531'),
            ('disk', 'fake', 'SMART/Throughput_Performance(2)/value', '100'),
            ('disk', 'fake', 'SMART/Throughput_Performance(2)/worst', '100'),
            ('disk', 'fake', 'SMART/Throughput_Performance(2)/thresh', '000'),
            ('disk', 'fake', 'SMART/Throughput_Performance(2)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Throughput_Performance(2)/raw',
             ' 33882636'),
            ('disk', 'fake', 'SMART/Spin_Up_Time(3)/value', '100'),
            ('disk', 'fake', 'SMART/Spin_Up_Time(3)/worst', '100'),
            ('disk', 'fake', 'SMART/Spin_Up_Time(3)/thresh', '025'),
            ('disk', 'fake', 'SMART/Spin_Up_Time(3)/when_failed', 'NEVER'),
            ('disk', 'fake', 'SMART/Spin_Up_Time(3)/raw', ' 2'),
            ('disk', 'fake', 'SMART/Start_Stop_Count(4)/value', '100'),
            ('disk', 'fake', 'SMART/Start_Stop_Count(4)/worst', '100'),
            ('disk', 'fake', 'SMART/Start_Stop_Count(4)/thresh', '000'),
            ('disk', 'fake', 'SMART/Start_Stop_Count(4)/when_failed', 'NEVER'),
            ('disk', 'fake', 'SMART/Start_Stop_Count(4)/raw', ' 36'),
            ('disk', 'fake', 'SMART/Reallocated_Sector_Ct(5)/value', '100'),
            ('disk', 'fake', 'SMART/Reallocated_Sector_Ct(5)/worst', '100'),
            ('disk', 'fake', 'SMART/Reallocated_Sector_Ct(5)/thresh', '024'),
            ('disk', 'fake', 'SMART/Reallocated_Sector_Ct(5)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Reallocated_Sector_Ct(5)/raw',
             ' 0 (2000 0)'),
            ('disk', 'fake', 'SMART/Seek_Error_Rate(7)/value', '100'),
            ('disk', 'fake', 'SMART/Seek_Error_Rate(7)/worst', '100'),
            ('disk', 'fake', 'SMART/Seek_Error_Rate(7)/thresh', '000'),
            ('disk', 'fake', 'SMART/Seek_Error_Rate(7)/when_failed', 'NEVER'),
            ('disk', 'fake', 'SMART/Seek_Error_Rate(7)/raw', ' 1190'),
            ('disk', 'fake', 'SMART/Seek_Time_Performance(8)/value', '100'),
            ('disk', 'fake', 'SMART/Seek_Time_Performance(8)/worst', '100'),
            ('disk', 'fake', 'SMART/Seek_Time_Performance(8)/thresh', '000'),
            ('disk', 'fake', 'SMART/Seek_Time_Performance(8)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Seek_Time_Performance(8)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Power_On_Hours(9)/value', '001'),
            ('disk', 'fake', 'SMART/Power_On_Hours(9)/worst', '001'),
            ('disk', 'fake', 'SMART/Power_On_Hours(9)/thresh', '000'),
            ('disk', 'fake', 'SMART/Power_On_Hours(9)/when_failed', 'NEVER'),
            ('disk', 'fake', 'SMART/Power_On_Hours(9)/raw', ' 81676'),
            ('disk', 'fake', 'SMART/Spin_Retry_Count(10)/value', '100'),
            ('disk', 'fake', 'SMART/Spin_Retry_Count(10)/worst', '100'),
            ('disk', 'fake', 'SMART/Spin_Retry_Count(10)/thresh', '000'),
            ('disk', 'fake', 'SMART/Spin_Retry_Count(10)/when_failed', 'NEVER'),
            ('disk', 'fake', 'SMART/Spin_Retry_Count(10)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Power_Cycle_Count(12)/value', '100'),
            ('disk', 'fake', 'SMART/Power_Cycle_Count(12)/worst', '100'),
            ('disk', 'fake', 'SMART/Power_Cycle_Count(12)/thresh', '000'),
            ('disk', 'fake', 'SMART/Power_Cycle_Count(12)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Power_Cycle_Count(12)/raw', ' 36'),
            ('disk', 'fake', 'SMART/G-Sense_Error_Rate(191)/value', '100'),
            ('disk', 'fake', 'SMART/G-Sense_Error_Rate(191)/worst', '100'),
            ('disk', 'fake', 'SMART/G-Sense_Error_Rate(191)/thresh', '000'),
            ('disk', 'fake', 'SMART/G-Sense_Error_Rate(191)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/G-Sense_Error_Rate(191)/raw', ' 21'),
            ('disk', 'fake', 'SMART/Power-Off_Retract_Count(192)/value', '100'),
            ('disk', 'fake', 'SMART/Power-Off_Retract_Count(192)/worst', '100'),
            ('disk', 'fake', 'SMART/Power-Off_Retract_Count(192)/thresh',
             '000'),
            ('disk', 'fake', 'SMART/Power-Off_Retract_Count(192)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Power-Off_Retract_Count(192)/raw', ' 20'),
            ('disk', 'fake', 'SMART/Temperature_Celsius(194)/value', '100'),
            ('disk', 'fake', 'SMART/Temperature_Celsius(194)/worst', '100'),
            ('disk', 'fake', 'SMART/Temperature_Celsius(194)/thresh', '000'),
            ('disk', 'fake', 'SMART/Temperature_Celsius(194)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Temperature_Celsius(194)/raw',
             ' 20 (Min/Max 17/50)'),
            ('disk', 'fake', 'SMART/Hardware_ECC_Recovered(195)/value', '100'),
            ('disk', 'fake', 'SMART/Hardware_ECC_Recovered(195)/worst', '100'),
            ('disk', 'fake', 'SMART/Hardware_ECC_Recovered(195)/thresh', '000'),
            ('disk', 'fake', 'SMART/Hardware_ECC_Recovered(195)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Hardware_ECC_Recovered(195)/raw', ' 316'),
            ('disk', 'fake', 'SMART/Reallocated_Event_Count(196)/value', '100'),
            ('disk', 'fake', 'SMART/Reallocated_Event_Count(196)/worst', '100'),
            ('disk', 'fake', 'SMART/Reallocated_Event_Count(196)/thresh',
             '000'),
            ('disk', 'fake', 'SMART/Reallocated_Event_Count(196)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Reallocated_Event_Count(196)/raw',
             ' 0 (0 7014)'),
            ('disk', 'fake', 'SMART/Current_Pending_Sector(197)/value', '100'),
            ('disk', 'fake', 'SMART/Current_Pending_Sector(197)/worst', '100'),
            ('disk', 'fake', 'SMART/Current_Pending_Sector(197)/thresh', '000'),
            ('disk', 'fake', 'SMART/Current_Pending_Sector(197)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Current_Pending_Sector(197)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Offline_Uncorrectable(198)/value', '100'),
            ('disk', 'fake', 'SMART/Offline_Uncorrectable(198)/worst', '100'),
            ('disk', 'fake', 'SMART/Offline_Uncorrectable(198)/thresh', '000'),
            ('disk', 'fake', 'SMART/Offline_Uncorrectable(198)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Offline_Uncorrectable(198)/raw', ' 0'),
            ('disk', 'fake', 'SMART/UDMA_CRC_Error_Count(199)/value', '200'),
            ('disk', 'fake', 'SMART/UDMA_CRC_Error_Count(199)/worst', '253'),
            ('disk', 'fake', 'SMART/UDMA_CRC_Error_Count(199)/thresh', '000'),
            ('disk', 'fake', 'SMART/UDMA_CRC_Error_Count(199)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/UDMA_CRC_Error_Count(199)/raw', ' 8'),
            ('disk', 'fake', 'SMART/Multi_Zone_Error_Rate(200)/value', '100'),
            ('disk', 'fake', 'SMART/Multi_Zone_Error_Rate(200)/worst', '100'),
            ('disk', 'fake', 'SMART/Multi_Zone_Error_Rate(200)/thresh', '000'),
            ('disk', 'fake', 'SMART/Multi_Zone_Error_Rate(200)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Multi_Zone_Error_Rate(200)/raw', ' 9964'),
            ('disk', 'fake', 'SMART/Soft_Read_Error_Rate(201)/value', '100'),
            ('disk', 'fake', 'SMART/Soft_Read_Error_Rate(201)/worst', '100'),
            ('disk', 'fake', 'SMART/Soft_Read_Error_Rate(201)/thresh', '000'),
            ('disk', 'fake', 'SMART/Soft_Read_Error_Rate(201)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Soft_Read_Error_Rate(201)/raw', ' 0'),
            ('disk', 'fake', 'SMART/Run_Out_Cancel(203)/value', '100'),
            ('disk', 'fake', 'SMART/Run_Out_Cancel(203)/worst', '100'),
            ('disk', 'fake', 'SMART/Run_Out_Cancel(203)/thresh', '000'),
            ('disk', 'fake', 'SMART/Run_Out_Cancel(203)/when_failed', 'NEVER'),
            ('disk', 'fake', 'SMART/Run_Out_Cancel(203)/raw', ' 429541685302'),
            ('disk', 'fake', 'SMART/Load_Cycle_Count(225)/value', '100'),
            ('disk', 'fake', 'SMART/Load_Cycle_Count(225)/worst', '100'),
            ('disk', 'fake', 'SMART/Load_Cycle_Count(225)/thresh', '000'),
            ('disk', 'fake', 'SMART/Load_Cycle_Count(225)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Load_Cycle_Count(225)/raw', ' 19653'),
            ('disk', 'fake', 'SMART/Head_Flying_Hours(240)/value', '200'),
            ('disk', 'fake', 'SMART/Head_Flying_Hours(240)/worst', '200'),
            ('disk', 'fake', 'SMART/Head_Flying_Hours(240)/thresh', '000'),
            ('disk', 'fake', 'SMART/Head_Flying_Hours(240)/when_failed',
             'NEVER'),
            ('disk', 'fake', 'SMART/Head_Flying_Hours(240)/raw', ' 0')]


def read_smart_nvme_result():
    return [('disk', 'fake_nvme', 'SMART/model_number',
             'Samsung SSD 950 PRO 256GB'),
            ('disk', 'fake_nvme', 'SMART/serial_number', 'CYBERDYNE_T1000'),
            ('disk', 'fake_nvme', 'SMART/firmware_version', '1B0QBXX7'),
            ('disk', 'fake_nvme', 'SMART/critical_warning', '0x00'),
            ('disk', 'fake_nvme', 'SMART/temperature', '40'),
            ('disk', 'fake_nvme', 'SMART/temperature_unit', 'Celsius'),
            ('disk', 'fake_nvme', 'SMART/power_cycles', '32'),
            ('disk', 'fake_nvme', 'SMART/power_on_hours', '129'),
            ('disk', 'fake_nvme', 'SMART/unsafe_shutdowns', '6'),
            ('disk', 'fake_nvme', 'SMART/media_data_integrity_errors', '0'),
            ('disk', 'fake_nvme', 'SMART/error_information_log_entries', '44')]
