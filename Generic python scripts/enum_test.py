import enum


class System(enum.Enum):

    A = ('aa', (105, 106, 107, 111, 112, 113, 483), 30)
    B = ('bb', (480, 481, 482, ))
    C = ('cc', (484, 485, 486))
    D = ('dd', (1,))


    def __init__(self, label, ids, buffer_days=10):
        self._value_ = label
        self.ids = ids
        self.buffer_days = buffer_days

    def __str__(self) -> str:
        return self._value_

    def contains(self, ids):
        dcid = ids if isinstance(ids, int) else int(ids)
        return dcid in self.ids

    @ classmethod
    def from_ids(cls, dcid: str):
        dcid = dcid if isinstance(dcid, int) else int(dcid)
        for system in list(System):
            if dcid in system.ids:
                return system

        return None

if __name__ == '__main__':
    print(System.__name__)
    print(System._member_names_)
    print(System._value2member_map_)
    print([member.value for member in System])
    for member in System:
        print(member._value_ , member.ids)

    if 'aa' != System.A:
        print("ok")
        
    # Given list of supported systems
    supported_system_list = [System.A, System.B, System.C]

    # Get list of ids corresponding to those systems
    ids_list1 = [id for system in supported_system_list for id in system.ids]
    print(f"ids_list version 1- {ids_list1}")   

    ids_list2 = [system.ids for system in supported_system_list]
    print(f"ids_list version 2- {ids_list2}")   
