/* mbed Microcontroller Library
 * Copyright (c) 2006-2020 ARM Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/* MBED_DEPRECATED */
#warning "These services are deprecated and will be removed. Please see services.md for details about replacement services."

#ifndef MBED_BLE_MAGNETO_SERVICE_H__
#define MBED_BLE_MAGNETO_SERVICE_H__

#include "ble/BLE.h"
#include "ble/Gap.h"
#include "ble/GattServer.h"

#include <cmath>
#include <cstdint>

#if BLE_FEATURE_GATT_SERVER

class MagnetometerService {
public:
    MagnetometerService(BLE &_ble, uint16_t MX, uint16_t MY, uint16_t MZ) :
        ble(_ble),
        valueBytes(MX,MY,MZ),
        magnetoXYZ(
            GattCharacteristic::UUID_MAGNETO_MEASUREMENT_CHAR,
            (uint8_t*)valueBytes.getPointer(),
            valueBytes.getNumValueBytes(),
            valueBytes.getNumValueBytes(),
            GattCharacteristic::BLE_GATT_CHAR_PROPERTIES_NOTIFY
        )
    {
        setupService();
    }

    void updateMagnometerRate(int16_t MX, int16_t MY, int16_t MZ) {
        valueBytes.updateMRate(MX, MY, MZ);
        ble.gattServer().write(
            magnetoXYZ.getValueHandle(),
            (uint8_t*)valueBytes.getPointer(),
            valueBytes.getNumValueBytes()
        );
    }

protected:
    /**
     * Construct and add to the GattServer the heart rate service.
     */
    void setupService() {
        GattCharacteristic *charTable[] = {
            &magnetoXYZ,
        };
        GattService magnetoService(
            GattService::UUID_MAGNETO_SERVICE,
            charTable,
            sizeof(charTable) / sizeof(charTable[0])
        );

        ble.gattServer().addService(magnetoService);
    }

protected:

    struct MagnetoValueBytes {
        static const unsigned MAGNETO_NUM = 3;
        static const unsigned MAGNETO_X_IDX = 0;
        static const unsigned MAGNETO_Y_IDX = 1;
        static const unsigned MAGNETO_Z_IDX = 2;

        MagnetoValueBytes(int16_t MX, int16_t MY, int16_t MZ) : valueBytes()
        {
            updateMRate(MX, MY, MZ);
        }

        void updateMRate(int16_t MX, int16_t MY, int16_t MZ)
        {
            //valueBytes[MAGNETO_X_IDX] = MX;
            //valueBytes[MAGNETO_Y_IDX] = MY;
            //valueBytes[MAGNETO_Z_IDX] = MZ;
            valueBytes[0] = MX & 0xff;
            valueBytes[1] = (MX >> 8) & 0xff;
            valueBytes[2] = MY & 0xff;
            valueBytes[3] = (MY >> 8) & 0xff;
            valueBytes[4] = MZ & 0xff;
            valueBytes[5] = (MZ >> 8) & 0xff;
        }

        uint8_t *getPointer()
        {
            return valueBytes;
        }

        const uint8_t *getPointer() const
        {
            return valueBytes;
        }

        unsigned getNumValueBytes() const
        {
            return sizeof(int16_t) * MAGNETO_NUM; // 3 * 2 = 6 bytes
            //return 1 + sizeof(int16_t)*MAGNETO_NUM;
        }

    private:
        uint8_t valueBytes[2 * MAGNETO_NUM];  // Array to hold 6 bytes (2 bytes per each axis value)
        //int16_t valueBytes[MAGNETO_NUM];
    };
    

protected:
    BLE &ble;
    MagnetoValueBytes valueBytes;
    GattCharacteristic magnetoXYZ;
};

#endif // BLE_FEATURE_GATT_SERVER

#endif /* #ifndef MBED_BLE_HEART_RATE_SERVICE_H__*/
