package lab0_201_06.uwaterloo.ca.lab1_201_06;

import android.graphics.Color;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.LinearLayout;
import android.widget.TextView;



public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        findViewById(R.id.label1);
        LinearLayout l = (LinearLayout) findViewById(R.id.label2);
        l.setOrientation(LinearLayout.VERTICAL);
        TextView tv = (TextView) findViewById(R.id.label1);

        TextView tv1 = new TextView(getApplicationContext());
        tv.setText("I’ve replaced the label!");
        tv1.setText("This is another label!");
        tv1.setTextColor(Color.BLACK);
        l.addView(tv1);

        TextView tv3 = (TextView) findViewById(R.id.lightLabel);


        SensorManager sensorManager = (SensorManager) getSystemService(SENSOR_SERVICE);

        Sensor lightSensor = sensorManager.getDefaultSensor(Sensor.TYPE_LIGHT);

        SensorEventListener ll = new LightSensorEventListener(tv3);
        sensorManager.registerListener(ll, lightSensor, SensorManager.SENSOR_DELAY_NORMAL);
    }
}

class LightSensorEventListener implements SensorEventListener {
    TextView output;

    public LightSensorEventListener(TextView outputView) {
        output = outputView;
    }
    public void onAccuracyChanged(Sensor s, int i) {}

    public void onSensorChanged(SensorEvent se) {
        if (se.sensor.getType() == Sensor.TYPE_LIGHT) {
            double lightValue = se.values[0];

            // the variable se.values is an array of type int[] or double[]
            // the first value (se.values[0]) contains the value
            // of the light sensor. store it somewhere useful
        }
    }
}
