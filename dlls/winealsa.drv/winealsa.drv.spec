# WinMM driver functions
@ stdcall -private DriverProc(long long long long long) ALSA_DriverProc
@ stdcall -private midMessage(long long long long long) ALSA_midMessage
@ stdcall -private modMessage(long long long long long) ALSA_modMessage

# MMDevAPI driver functions
@ stdcall -private get_device_name_from_guid(ptr ptr ptr) get_device_name_from_guid
@ stdcall -private GetEndpointIDs(long ptr ptr ptr ptr) AUDDRV_GetEndpointIDs
@ stdcall -private GetPropValue(ptr ptr ptr) AUDDRV_GetPropValue
