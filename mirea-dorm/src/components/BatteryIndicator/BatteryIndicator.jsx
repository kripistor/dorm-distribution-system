import React from 'react';
import styles from './BatteryIndicator.module.css';

const BatteryIndicator = ({percent}) => {
    const getBatteryColor = () => {
        if (percent >= 70) {
            return '#FF5D5D';
        } else if (percent >= 50) {
            return '#FFAD4D';
        } else if (percent >= 30) {
            return '#FFD954';
        } else {
            return '#2CAA00';
        }
    };

    const renderBatteryBars = () => {
        const bars = [];
        const numBars = 10;

        if (percent === 0) {
            bars.push(<div key={0} className={styles.battery_bar} style={{backgroundColor: 'green'}}></div>);
            for (let i = 1; i < numBars; i++) {
                bars.push(<div key={i} className={styles.battery_bar} style={{backgroundColor: 'transparent'}}></div>);
            }
        }
        else {
            for (let i = 0; i < numBars; i++) {
                const barStyle = {
                    backgroundColor: i < (percent / 10) ? getBatteryColor() : 'transparent',
                };

                bars.push(<div key={i} className={styles.battery_bar} style={barStyle}></div>);
            }
        }

        return bars;
    };

    return (
        <div className={styles.battery_indicator}>
            {renderBatteryBars()}
        </div>
    );
};

export default BatteryIndicator;
