from typing import Any
from abc import abstractmethod


class Stat:
    def __init__(self, name: str):
        self._name = name
        self._value = None

    @abstractmethod
    def set_value_from_stat_file(self, stat_file):
        raise NotImplementedError

    def set_value(self, value: Any):
        if not self._value is None:
            raise ValueError("_value is already set.")
        self._value = value

    def get_value(self):
        if self._value == None:
            raise ValueError("_value has not been set yet.")
        return self._value

    def reset(self):
        if self._value is None:
            raise ValueError("_value has not been set yet.")
        self._value = None

    def __str__(self):
        return f"{self._name}={self._value}"


class RootStat(Stat):
    def __init__(self, name: str):
        super().__init__(name)

    def set_value_from_stat_file(self, stat_file):
        ret = 0
        instances = 0
        stat_file.seek(0)
        for line in stat_file.readlines()[2:10]:
            stat_in_line = line.split()[0]
            if self._name == stat_in_line:
                ret = float(line.split()[1])
                instances += 1
        if instances == 0:
            raise ValueError(
                f"Could not find {self._name} in {stat_file.name}"
            )
        self._value = ret


class AggregateStat(Stat):
    def __init__(self, name: str):
        super().__init__(name)

    def set_value_from_stat_file(self, stat_file):
        ret = 0
        instances = 0
        stat_file.seek(0)
        for line in stat_file.readlines()[10:-3]:
            stat_in_line = line.split()[0].split(".")[-1]
            if self._name == stat_in_line:
                ret += float(line.split()[1])
                instances += 1
        if instances == 0:
            raise ValueError(
                f"Could not find {self._name} in {stat_file.name}"
            )
        self._value = ret
