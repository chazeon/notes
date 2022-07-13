---
title: Blender MD Visualization
---

Blender opens up excellent opportunities for MD visualization by offering latest Python interpreter out-of-box. However, large number of atoms and large number of MD time steps make adding atoms and trajectories difficult. However, there are specific way of programming that allows you to achieve much improved performance.

### Large number of atoms

Creating objects using copy instead of `bpy.ops.mesh.primitive_xxx_add`.

```python
bpy.ops.mesh.primitive_uv_sphere_add(radius=.04)
refobj = bpy.context.object

for i in range(natoms):
  sphere = bpy.data.objects.new(f"atom{i:04d}", refobj.data.copy())
  collections[atype].objects.link(sphere)
```

### Long MD trajectory

Use `foreach_set` instead of `keyframe_insert`.

```python
coords = []
iframes = range(len(coords))

sphere.location = tuple(coords * self.scale)
sphere.keyframe_insert(data_path="location", frame=frame_current)

fcurves = sphere.animation_data.action.fcurves

for k in range(3):
  fcurve = fcurves.find("location", index=k)
  fcurve.keyframe_points.add(count=len(iframes))
  fcurve.keyframe_points.foreach_set("co", [
      x
      for pair in zip(iframes, coords[:,k])
      for x in pair
  ])            
```

### Memory usage

After addressing the two issues above, the final limiting factor would be memory. Get prepared, 8192 atoms consume ~35 GB memory.

## References

- [Blender Operator Translations | Moo-Ack! Productions (theduckcow.com)](https://theduckcow.com/dev/blender/operator-translations/)
- [python - Editing fcurve.keyframe points in FAST mode? - Blender Stack Exchange](https://blender.stackexchange.com/questions/92287/editing-fcurve-keyframe-points-in-fast-mode)

