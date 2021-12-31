const findMedianSortedArrays = (nums1, nums2) => {
  let a;
  let b;
  if (nums1.length <= nums2.length) {
    a = nums1;
    b = nums2;
  } else {
    a = nums2;
    b = nums1;
  }

  let totalLen = a.length + b.length;
  let half = Math.floor((a.length + b.length) / 2);
  let left_pointer = 0;
  let right_pointer = a.length - 1;
  while (true) {
    a_mid = Math.round((left_pointer + right_pointer) / 2);
    b_mid = half - a_mid - 2;

    console.log({ a_mid }, { b_mid }, { half }, "here");

    let aMidElement = a_mid >= 0 ? a[a_mid] : parseFloat(-Infinity);
    let aNextToMid = a_mid + 1 < a.length ? a[a_mid + 1] : Infinity;
    let bMidElement = b_mid >= 0 ? b[b_mid] : parseFloat(-Infinity);
    let bNextToMid = b_mid + 1 < b.length ? a[a_mid + 1] : Infinity;

    console.log(
      { aMidElement },
      { aNextToMid },
      { bMidElement },
      { bNextToMid },
      "here2"
    );

    if (aMidElement <= bNextToMid && bMidElement <= aNextToMid) {
      if (totalLen % 2 == 0) {
        console.log(Math.min(aNextToMid, bNextToMid));
        console.log(Math.max(aMidElement, bMidElement));
        return (
          (Math.max(aMidElement, bMidElement) +
            Math.min(aNextToMid, bNextToMid)) /
          2
        ).toFixed(2);
      }
      return Math.min(aNextToMid, bNextToMid);
    } else if (aMidElement < bNextToMid) {
      right_pointer = a_mid - 1;
    } else {
      left_pointer = a_mid + 1;
    }
  }
};

// console.log(findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4]));
// 1,1,2,2,3,3,4,4,5,6,7,8
console.log();
findMedianSortedArrays([0, 0], [0, 0]);
