class Picmg:
    PICMG_LINK_INTERFACE_BASE           = 0x0
    PICMG_LINK_INTERFACE_FABRIC         = 0x1
    PICMG_LINK_INTERFACE_UPDATE_CHANNEL = 0x2

    PICMG_LINK_TYPE_BASE              = 0x01
    PICMG_LINK_TYPE_ETHERNET_FABRIC   = 0x02
    PICMG_LINK_TYPE_INFINIBAND_FABRIC = 0x03
    PICMG_LINK_TYPE_STARFABRIC_FABRIC = 0x04
    PICMG_LINK_TYPE_PCIEXPRESS_FABRIC = 0x05

    PICMG_LINK_TYPE_EXT_BASE0 = 0x00
    PICMG_LINK_TYPE_EXT_BASE1 = 0x01

    PICMG_LINK_TYPE_EXT_ETHERNET_FIX1000BX       = 0x00
    PICMG_LINK_TYPE_EXT_ETHERNET_FIX10GBX4       = 0x01
    PICMG_LINK_TYPE_EXT_ETHERNET_FCPI            = 0x02
    PICMG_LINK_TYPE_EXT_ETHERNET_FIX1000KX_10GKR = 0x03
    PICMG_LINK_TYPE_EXT_ETHERNET_FIX10GKX4       = 0x04
    PICMG_LINK_TYPE_EXT_ETHERNET_FIX40GKR4       = 0x05

    PICMG_LINK_FLAGS_LANE0    = 0x01
    PICMG_LINK_FLAGS_LANE0123 = 0x0f

    PICMG_LINK_STATE_DISABLE  = 0
    PICMG_LINK_STATE_ENABLE   = 1

    PICMG_CHANNEL_SIGNALING_CLASS_BASIC = 0
    PICMG_CHANNEL_SIGNALING_CLASS_10_3125GBD = 4
