# License: MIT
# Copyright © 2023 Frequenz Energy-as-a-Service GmbH

"""Wrappers for the ComponentData.

This module allows the easy construction of mock ComponentData instances to be used in
unit tests. Usually, all parameters for an instance need to be defined, this module
helps by allowing users to only specify the parameters they are interested in for their
tests. The rest will be filled with default protobuf values.
This also abstracts away changes in the protobuf definition and minimizes the places
that will need to be updated in such cases.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, replace
from datetime import datetime

import frequenz.api.microgrid.battery_pb2 as battery_pb
import frequenz.api.microgrid.inverter_pb2 as inverter_pb
from frequenz.client.microgrid import (
    BatteryData,
    EVChargerCableState,
    EVChargerComponentState,
    EVChargerData,
    InverterData,
    MeterData,
)

# pylint: disable=no-member


class BatteryDataWrapper(BatteryData):
    """Wrapper for the BatteryData with default arguments."""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        component_id: int,
        timestamp: datetime,
        soc: float = math.nan,
        soc_lower_bound: float = math.nan,
        soc_upper_bound: float = math.nan,
        capacity: float = math.nan,
        power_inclusion_lower_bound: float = math.nan,
        power_exclusion_lower_bound: float = math.nan,
        power_inclusion_upper_bound: float = math.nan,
        power_exclusion_upper_bound: float = math.nan,
        temperature: float = math.nan,
        _relay_state: battery_pb.RelayState.ValueType = (
            battery_pb.RelayState.RELAY_STATE_UNSPECIFIED
        ),
        _component_state: battery_pb.ComponentState.ValueType = (
            battery_pb.ComponentState.COMPONENT_STATE_UNSPECIFIED
        ),
        _errors: list[battery_pb.Error] | None = None,
    ) -> None:
        """Initialize the BatteryDataWrapper.

        This is a wrapper for the BatteryData with default arguments. The parameters are
        documented in the BatteryData class.
        """
        super().__init__(
            component_id=component_id,
            timestamp=timestamp,
            soc=soc,
            soc_lower_bound=soc_lower_bound,
            soc_upper_bound=soc_upper_bound,
            capacity=capacity,
            power_inclusion_lower_bound=power_inclusion_lower_bound,
            power_exclusion_lower_bound=power_exclusion_lower_bound,
            power_inclusion_upper_bound=power_inclusion_upper_bound,
            power_exclusion_upper_bound=power_exclusion_upper_bound,
            temperature=temperature,
            _relay_state=_relay_state,
            _component_state=_component_state,
            _errors=_errors if _errors else [],
        )

    def copy_with_new_timestamp(self, new_timestamp: datetime) -> BatteryDataWrapper:
        """Copy the component data but insert new timestamp.

        Because the dataclass is frozen, we can't just replace the timestamp.
        We have to copy it.

        Args:
            new_timestamp: New timestamp.

        Returns:
            Copied component data.
        """
        return replace(self, timestamp=new_timestamp)


@dataclass(frozen=True)
class InverterDataWrapper(InverterData):
    """Wrapper for the InverterData with default arguments."""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        component_id: int,
        timestamp: datetime,
        active_power: float = math.nan,
        active_power_per_phase: tuple[float, float, float] = (
            math.nan,
            math.nan,
            math.nan,
        ),
        current_per_phase: tuple[float, float, float] = (math.nan, math.nan, math.nan),
        voltage_per_phase: tuple[float, float, float] = (math.nan, math.nan, math.nan),
        active_power_inclusion_lower_bound: float = math.nan,
        active_power_exclusion_lower_bound: float = math.nan,
        active_power_inclusion_upper_bound: float = math.nan,
        active_power_exclusion_upper_bound: float = math.nan,
        reactive_power: float = math.nan,
        reactive_power_per_phase: tuple[float, float, float] = (
            math.nan,
            math.nan,
            math.nan,
        ),
        frequency: float = 50.0,
        _component_state: inverter_pb.ComponentState.ValueType = (
            inverter_pb.ComponentState.COMPONENT_STATE_UNSPECIFIED
        ),
        _errors: list[inverter_pb.Error] | None = None,
    ) -> None:
        """Initialize the InverterDataWrapper.

        This is a wrapper for the InverterData with default arguments. The parameters
        are documented in the InverterData class.
        """
        super().__init__(
            component_id=component_id,
            timestamp=timestamp,
            active_power=active_power,
            active_power_per_phase=active_power_per_phase,
            current_per_phase=current_per_phase,
            voltage_per_phase=voltage_per_phase,
            active_power_inclusion_lower_bound=active_power_inclusion_lower_bound,
            active_power_exclusion_lower_bound=active_power_exclusion_lower_bound,
            active_power_inclusion_upper_bound=active_power_inclusion_upper_bound,
            active_power_exclusion_upper_bound=active_power_exclusion_upper_bound,
            reactive_power=reactive_power,
            reactive_power_per_phase=reactive_power_per_phase,
            _component_state=_component_state,
            frequency=frequency,
            _errors=_errors if _errors else [],
        )

    def copy_with_new_timestamp(self, new_timestamp: datetime) -> InverterDataWrapper:
        """Copy the component data but insert new timestamp.

        Because the dataclass is frozen, we can't just replace the timestamp.
        We have to copy it.

        Args:
            new_timestamp: New timestamp.

        Returns:
            Copied component data.
        """
        return replace(self, timestamp=new_timestamp)


@dataclass(frozen=True)
class EvChargerDataWrapper(EVChargerData):
    """Wrapper for the EvChargerData with default arguments."""

    def __init__(  # pylint: disable=too-many-arguments,too-many-locals
        self,
        component_id: int,
        timestamp: datetime,
        active_power: float = math.nan,
        active_power_per_phase: tuple[float, float, float] = (
            math.nan,
            math.nan,
            math.nan,
        ),
        current_per_phase: tuple[float, float, float] = (math.nan, math.nan, math.nan),
        voltage_per_phase: tuple[float, float, float] = (math.nan, math.nan, math.nan),
        active_power_inclusion_lower_bound: float = math.nan,
        active_power_exclusion_lower_bound: float = math.nan,
        active_power_inclusion_upper_bound: float = math.nan,
        active_power_exclusion_upper_bound: float = math.nan,
        reactive_power: float = math.nan,
        reactive_power_per_phase: tuple[float, float, float] = (
            math.nan,
            math.nan,
            math.nan,
        ),
        frequency: float = 50.0,
        cable_state: EVChargerCableState = EVChargerCableState.UNSPECIFIED,
        component_state: EVChargerComponentState = EVChargerComponentState.UNSPECIFIED,
    ) -> None:
        """Initialize the EvChargerDataWrapper.

        This is a wrapper for the EvChargerData with default arguments. The parameters
        are documented in the EvChargerData class.
        """
        super().__init__(
            component_id=component_id,
            timestamp=timestamp,
            active_power=active_power,
            active_power_per_phase=active_power_per_phase,
            current_per_phase=current_per_phase,
            voltage_per_phase=voltage_per_phase,
            active_power_inclusion_lower_bound=active_power_inclusion_lower_bound,
            active_power_exclusion_lower_bound=active_power_exclusion_lower_bound,
            active_power_inclusion_upper_bound=active_power_inclusion_upper_bound,
            active_power_exclusion_upper_bound=active_power_exclusion_upper_bound,
            reactive_power=reactive_power,
            reactive_power_per_phase=reactive_power_per_phase,
            frequency=frequency,
            cable_state=cable_state,
            component_state=component_state,
        )

    def copy_with_new_timestamp(self, new_timestamp: datetime) -> EvChargerDataWrapper:
        """Copy the component data but insert new timestamp.

        Because the dataclass is frozen, we can't just replace the timestamp.
        We have to copy it.

        Args:
            new_timestamp: New timestamp.

        Returns:
            Copied component data.
        """
        return replace(self, timestamp=new_timestamp)


@dataclass(frozen=True)
class MeterDataWrapper(MeterData):
    """Wrapper for the MeterData with default arguments."""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        component_id: int,
        timestamp: datetime,
        active_power: float = math.nan,
        active_power_per_phase: tuple[float, float, float] = (
            math.nan,
            math.nan,
            math.nan,
        ),
        reactive_power: float = math.nan,
        reactive_power_per_phase: tuple[float, float, float] = (
            math.nan,
            math.nan,
            math.nan,
        ),
        current_per_phase: tuple[float, float, float] = (math.nan, math.nan, math.nan),
        voltage_per_phase: tuple[float, float, float] = (math.nan, math.nan, math.nan),
        frequency: float = math.nan,
    ) -> None:
        """Initialize the MeterDataWrapper.

        This is a wrapper for the MeterData with default arguments. The parameters are
        documented in the MeterData class.
        """
        super().__init__(
            component_id=component_id,
            timestamp=timestamp,
            active_power=active_power,
            active_power_per_phase=active_power_per_phase,
            reactive_power=reactive_power,
            reactive_power_per_phase=reactive_power_per_phase,
            current_per_phase=current_per_phase,
            voltage_per_phase=voltage_per_phase,
            frequency=frequency,
        )

    def copy_with_new_timestamp(self, new_timestamp: datetime) -> MeterDataWrapper:
        """Copy the component data but insert new timestamp.

        Because the dataclass is frozen, we can't just replace the timestamp.
        We have to copy it.

        Args:
            new_timestamp: New timestamp.

        Returns:
            Copied component data.
        """
        return replace(self, timestamp=new_timestamp)
