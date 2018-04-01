feb 28, 2017
# Tags for com.getsentry.raven for Android

I couldn’t figure out how to add tags or anything to my captured exceptions for Android, which led them to be rather bland/unhelpful when trying to pin down what was causing a bug on the Android camera (notorious for being inconsistent across manufacturers, devices, Android versions, etc.)

I ended up doing the following, which hopefully helps others!

    import com.getsentry.raven.android.Raven;
    import com.getsentry.raven.event.EventBuilder;
    import com.getsentry.raven.event.helper.EventBuilderHelper

    ...

    Raven.init(this.getApplicationContext());
    try {
      Field f = Raven.class.getDeclaredField("raven");
      f.setAccessible(true);
      com.getsentry.raven.Raven raven = (com.getsentry.raven.Raven) f.get(Raven.class);
      final ConnectivityManager connManager = (ConnectivityManager) getSystemService(CONNECTIVITY_SERVICE);
      final NetworkInfo mWifi = connManager.getNetworkInfo(ConnectivityManager.TYPE_WIFI);
      final PackageInfo pInfo = getPackageManager().getPackageInfo(getPackageName(), 0);;
      raven.addBuilderHelper(new EventBuilderHelper() {
          [@Override](http://twitter.com/Override)
          public void helpBuildingEvent(EventBuilder eventBuilder) {
            eventBuilder.withTag("wifi", String.valueOf(mWifi.isConnected()));
            eventBuilder.withTag("app_version", pInfo.versionName);
            eventBuilder.withTag("build_version", Build.VERSION.RELEASE);
            eventBuilder.withTag("build_manufacturer", Build.MANUFACTURER);
            eventBuilder.withTag("build_brand", Build.BRAND);
            eventBuilder.withTag("build_device", Build.DEVICE);
            eventBuilder.withTag("build_product", Build.PRODUCT);
            eventBuilder.withTag("debug_app", BuildConfig.DEBUG ? "true" : "false");
            eventBuilder.withTag("build_brand", Build.BRAND);
          }
      });
    } catch (Exception e) {
      Raven.capture(e);
    }

Obviously you can see the pattern here to add tags using the eventBuilder. I have no idea why this was omitted in the Android version of Raven, but reflection saves the day per usual.
